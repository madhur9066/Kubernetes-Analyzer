"""
k8s_module.py — Kubernetes client, serializers, cluster registry.
Kubeconfig stored as YAML string in clusters.json — no file paths.
"""

import json
import os
import tempfile
from datetime import datetime, timezone

try:
    from kubernetes import client, config as k8s_config
    from kubernetes.client.rest import ApiException
    K8S_AVAILABLE = True
except ImportError:
    K8S_AVAILABLE = False

CLUSTERS_FILE = "clusters.json"


# ── Registry ──────────────────────────────────
def load_clusters(path=CLUSTERS_FILE):
    try:
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
    except Exception:
        pass
    return []


def save_clusters(clusters, path=CLUSTERS_FILE):
    with open(path, "w") as f:
        json.dump(clusters, f, indent=2)


# ── Helpers ───────────────────────────────────
def age(ts) -> str:
    if not ts:
        return "—"
    now = datetime.now(timezone.utc)
    delta = now - (ts.replace(tzinfo=timezone.utc) if ts.tzinfo is None else ts)
    s = int(delta.total_seconds())
    if s < 60:    return f"{s}s"
    if s < 3600:  return f"{s//60}m"
    if s < 86400: return f"{s//3600}h"
    return f"{s//86400}d"


def pod_ready_count(pod):
    st = pod.status.container_statuses or []
    return sum(1 for c in st if c.ready), len(st)


def best_ts(e):
    return (e.last_timestamp or e.first_timestamp
            or e.metadata.creation_timestamp
            or datetime.min.replace(tzinfo=timezone.utc))


# ── K8s Client ────────────────────────────────
def _needs_ssl_skip(kubeconfig_data: str) -> bool:
    """
    Return True when the cluster should skip TLS verification. Triggers when:
      - insecure-skip-tls-verify: true is set, OR
      - certificate-authority-data is absent, OR
      - server address is a private/internal IP (self-signed cert, no system CA)
    """
    import re as _re
    _PRIV = _re.compile(
        r"https?://(10[.]|172[.](1[6-9]|2[0-9]|3[01])[.]|192[.]168[.]|127[.]|localhost)"
    )
    try:
        import yaml
        kc      = yaml.safe_load(kubeconfig_data) or {}
        current = kc.get("current-context", "")
        ctx_obj = next(
            (c for c in kc.get("contexts", []) if c.get("name") == current), None
        )
        if not ctx_obj:
            return False
        cname  = (ctx_obj.get("context") or {}).get("cluster", "")
        cl_cfg = next(
            (c.get("cluster") or {} for c in kc.get("clusters", [])
             if c.get("name") == cname),
            {}
        )
        server = cl_cfg.get("server", "")
        return (
            bool(cl_cfg.get("insecure-skip-tls-verify", False))
            or not cl_cfg.get("certificate-authority-data", "")
            or bool(_PRIV.match(server))
        )
    except Exception:
        return False


class K8sClient:
    def __init__(self, kubeconfig_data: str, namespace: str = "default"):
        self.namespace    = namespace
        self._skip_tls    = _needs_ssl_skip(kubeconfig_data)

        # Write kubeconfig to a temp file (kubernetes-client requirement)
        self._tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False, prefix="k8s_")
        self._tmp.write(kubeconfig_data)
        self._tmp.flush()
        self._tmp_path = self._tmp.name
        self._tmp.close()

        # ── SSL fix ───────────────────────────────────────────────────────
        # load_kube_config populates the *global* default Configuration.
        # For self-signed / internal-CA clusters we must patch that config
        # immediately after loading it and before creating any API clients.
        # We also suppress urllib3's InsecureRequestWarning to keep logs clean.
        if self._skip_tls:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        k8s_config.load_kube_config(config_file=self._tmp_path)

        if self._skip_tls:
            # Works with kubernetes-client >= 12 (uses thread-local config)
            cfg = client.Configuration()
            k8s_config.load_kube_config(
                config_file=self._tmp_path,
                client_configuration=cfg,
            )
            cfg.verify_ssl  = False
            cfg.ssl_ca_cert = None
            api_client = client.ApiClient(configuration=cfg)
        else:
            api_client = client.ApiClient()

        self.core       = client.CoreV1Api(api_client=api_client)
        self.apps       = client.AppsV1Api(api_client=api_client)
        self.networking = client.NetworkingV1Api(api_client=api_client)

    def __del__(self):
        try:
            if hasattr(self, "_tmp_path") and os.path.exists(self._tmp_path):
                os.unlink(self._tmp_path)
        except Exception:
            pass

    def _api_client(self):
        """Return a per-instance ApiClient that respects SSL setting."""
        if self._skip_tls:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            cfg = client.Configuration()
            k8s_config.load_kube_config(
                config_file=self._tmp_path,
                client_configuration=cfg,
            )
            cfg.verify_ssl  = False
            cfg.ssl_ca_cert = None
            return client.ApiClient(configuration=cfg)
        return client.ApiClient()

    def get_cluster_name(self):
        try:
            ctx = k8s_config.list_kube_config_contexts(config_file=self._tmp_path)
            a   = ctx[1] if ctx and len(ctx) > 1 else {}
            return a.get("context", {}).get("cluster", "unknown") if isinstance(a, dict) else "unknown"
        except Exception:
            return "unknown"

    def get_server_version(self):
        try:
            return client.VersionApi(api_client=self._api_client()).get_code().git_version
        except Exception:
            return "unknown"

    def get_namespaces(self):
        return sorted([ns.metadata.name for ns in self.core.list_namespace().items])

    def get_nodes(self):
        return self.core.list_node().items

    def get_all_pods(self):
        return self.core.list_pod_for_all_namespaces().items

    def get_all_deployments(self):
        return self.apps.list_deployment_for_all_namespaces().items

    def get_all_statefulsets(self):
        return self.apps.list_stateful_set_for_all_namespaces().items

    def get_all_services(self):
        return self.core.list_service_for_all_namespaces().items

    def get_all_configmaps(self):
        return self.core.list_config_map_for_all_namespaces().items

    def get_all_secrets(self):
        return self.core.list_secret_for_all_namespaces().items

    def get_all_pvcs(self):
        return self.core.list_persistent_volume_claim_for_all_namespaces().items

    def get_all_ingresses(self):
        try:
            return self.networking.list_ingress_for_all_namespaces().items
        except Exception:
            return []

    def get_all_events(self):
        try:
            evts = self.core.list_event_for_all_namespaces().items
            return sorted(evts, key=best_ts, reverse=True)
        except Exception:
            return []

    def get_pods(self):
        return self.core.list_namespaced_pod(self.namespace).items

    def get_pod_logs(self, pod_name: str, tail: int = 200) -> str:
        try:
            return self.core.read_namespaced_pod_log(
                name=pod_name, namespace=self.namespace, tail_lines=tail)
        except ApiException as e:
            return f"Error: {e.reason}"

    def get_deployments(self):
        return self.apps.list_namespaced_deployment(self.namespace).items

    def get_statefulsets(self):
        return self.apps.list_namespaced_stateful_set(self.namespace).items

    def get_services(self):
        return self.core.list_namespaced_service(self.namespace).items

    def get_configmaps(self):
        return self.core.list_namespaced_config_map(self.namespace).items

    def get_secrets(self):
        return self.core.list_namespaced_secret(self.namespace).items

    def get_ingresses(self):
        try:
            return self.networking.list_namespaced_ingress(self.namespace).items
        except Exception:
            return []

    def get_pvcs(self):
        return self.core.list_namespaced_persistent_volume_claim(self.namespace).items

    def get_pvs(self):
        return self.core.list_persistent_volume().items

    def delete_pod(self, pod_name: str) -> dict:
        """Force-delete a pod."""
        try:
            self.core.delete_namespaced_pod(name=pod_name, namespace=self.namespace)
            return {"ok": True, "message": f"Pod '{pod_name}' deleted."}
        except ApiException as e:
            return {"ok": False, "error": f"API error {e.status}: {e.reason}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def delete_deployment(self, name: str) -> dict:
        """Delete a deployment."""
        try:
            self.apps.delete_namespaced_deployment(name=name, namespace=self.namespace)
            return {"ok": True, "message": f"Deployment '{name}' deleted."}
        except ApiException as e:
            return {"ok": False, "error": f"API error {e.status}: {e.reason}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def delete_statefulset(self, name: str) -> dict:
        """Delete a statefulset."""
        try:
            self.apps.delete_namespaced_stateful_set(name=name, namespace=self.namespace)
            return {"ok": True, "message": f"StatefulSet '{name}' deleted."}
        except ApiException as e:
            return {"ok": False, "error": f"API error {e.status}: {e.reason}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def restart_pod(self, pod_name: str) -> dict:
        """Restart a pod by deleting it (controller recreates it)."""
        try:
            self.core.delete_namespaced_pod(name=pod_name, namespace=self.namespace)
            return {"ok": True, "message": f"Pod '{pod_name}' deleted — will be recreated by its controller."}
        except ApiException as e:
            return {"ok": False, "error": f"API error {e.status}: {e.reason}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def rollout_restart_deployment(self, name: str) -> dict:
        """Trigger a rollout restart on a Deployment via annotation patch."""
        try:
            import datetime as _dt
            now = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            body = {
                "spec": {
                    "template": {
                        "metadata": {
                            "annotations": {
                                "kubectl.kubernetes.io/restartedAt": now
                            }
                        }
                    }
                }
            }
            self.apps.patch_namespaced_deployment(name=name, namespace=self.namespace, body=body)
            return {"ok": True, "message": f"Deployment '{name}' rollout restart triggered."}
        except ApiException as e:
            return {"ok": False, "error": f"API error {e.status}: {e.reason}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def rollout_restart_statefulset(self, name: str) -> dict:
        """Trigger a rollout restart on a StatefulSet via annotation patch."""
        try:
            import datetime as _dt
            now = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            body = {
                "spec": {
                    "template": {
                        "metadata": {
                            "annotations": {
                                "kubectl.kubernetes.io/restartedAt": now
                            }
                        }
                    }
                }
            }
            self.apps.patch_namespaced_stateful_set(name=name, namespace=self.namespace, body=body)
            return {"ok": True, "message": f"StatefulSet '{name}' rollout restart triggered."}
        except ApiException as e:
            return {"ok": False, "error": f"API error {e.status}: {e.reason}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def get_events(self, resource_name=None):
        evts = self.core.list_namespaced_event(self.namespace).items
        if resource_name:
            evts = [e for e in evts if e.involved_object.name == resource_name]
        return sorted(evts, key=best_ts, reverse=True)

    def get_cluster_overview(self):
        try:
            all_pods = self.get_all_pods()
            all_deps = self.get_all_deployments()
            nodes    = self.get_nodes()
            node_ready = sum(
                1 for n in nodes
                if any(c.type == "Ready" and c.status == "True"
                       for c in (n.status.conditions or []))
            )
            dep_healthy = sum(
                1 for d in all_deps
                if (d.status.ready_replicas or 0) == (d.spec.replicas or 0)
                and (d.spec.replicas or 0) > 0
            )
            return {
                "ok": True,
                "version":      self.get_server_version(),
                "cluster":      self.get_cluster_name(),
                "nodes":        len(nodes),
                "nodes_ready":  node_ready,
                "namespaces":   len(self.get_namespaces()),
                "pods":         len(all_pods),
                "pods_running": sum(1 for p in all_pods if (p.status.phase or "") == "Running"),
                "pods_pending": sum(1 for p in all_pods if (p.status.phase or "") == "Pending"),
                "pods_failed":  sum(1 for p in all_pods if (p.status.phase or "") == "Failed"),
                "deployments":  len(all_deps),
                "dep_healthy":  dep_healthy,
            }
        except Exception as e:
            return {"ok": False, "error": str(e)}


# ── Client cache (60s TTL) ────────────────────
import time as _time
_cache: dict = {}        # key -> K8sClient
_cache_ts: dict = {}     # key -> timestamp
_CACHE_TTL = 60          # seconds


def get_client(cluster_name: str, namespace: str, clusters_file=CLUSTERS_FILE):
    key = f"{cluster_name}::{namespace}"
    now = _time.time()
    # Expire stale entries
    if key in _cache and (now - _cache_ts.get(key, 0)) > _CACHE_TTL:
        del _cache[key]
        del _cache_ts[key]
    if key not in _cache:
        clusters = load_clusters(clusters_file)
        cl = next((c for c in clusters if c["name"] == cluster_name), None)
        if not cl:
            raise ValueError(f"Cluster '{cluster_name}' not found")
        kc = cl.get("kubeconfig_data", "")
        if not kc:
            raise ValueError(f"Cluster '{cluster_name}' has no kubeconfig — please re-add it.")
        _cache[key]    = K8sClient(kc, namespace)
        _cache_ts[key] = now
    return _cache[key]


def clear_cluster_cache(cluster_name: str):
    for key in list(_cache.keys()):
        if key.startswith(f"{cluster_name}::"):
            del _cache[key]
            _cache_ts.pop(key, None)


# ── Serializers ───────────────────────────────
def serialize_node(node):
    meta, spec, status = node.metadata, node.spec, node.status
    labels = meta.labels or {}
    roles  = [k.split("/", 1)[1] for k in labels
               if k.startswith("node-role.kubernetes.io/") and k.split("/", 1)[1]]
    if not roles:
        roles = ["worker"]
    conds    = status.conditions or []
    is_ready = any(c.type == "Ready" and c.status == "True" for c in conds)
    cap      = status.capacity    or {}
    alloc    = status.allocatable or {}
    info     = status.node_info   or {}
    addrs    = {a.type: a.address for a in (status.addresses or [])}
    return {
        "name":              meta.name,
        "age":               age(meta.creation_timestamp),
        "roles":             roles,
        "ready":             is_ready,
        "version":           getattr(info, "kubelet_version",           "—"),
        "os":                getattr(info, "os_image",                  "—"),
        "kernel":            getattr(info, "kernel_version",            "—"),
        "container_runtime": getattr(info, "container_runtime_version", "—"),
        "architecture":      getattr(info, "architecture",              "—"),
        "cpu_capacity":      cap.get("cpu",    "—"),
        "mem_capacity":      cap.get("memory", "—"),
        "cpu_allocatable":   alloc.get("cpu",    "—"),
        "mem_allocatable":   alloc.get("memory", "—"),
        "pods_capacity":     cap.get("pods",   "—"),
        "internal_ip":       addrs.get("InternalIP", "—"),
        "external_ip":       addrs.get("ExternalIP", "—"),
        "hostname":          addrs.get("Hostname",   "—"),
        "taints":            [{"key": t.key, "value": t.value or "", "effect": t.effect}
                               for t in (spec.taints or [])],
        "conditions":        [{"type": c.type, "status": c.status,
                                "reason": c.reason or "", "message": c.message or ""}
                               for c in conds],
        "labels":            {k: v for k, v in labels.items()
                               if not k.startswith("node-role.kubernetes.io/")},
        "unschedulable":     spec.unschedulable or False,
    }


def serialize_pod(pod):
    meta, spec, status = pod.metadata, pod.spec, pod.status
    phase = status.phase or "Unknown"
    ready, total = pod_ready_count(pod)
    containers = []
    for cs in (status.container_statuses or []):
        st = cs.state
        if st.running:      sstr = f"Running (started {age(st.running.started_at)} ago)"
        elif st.waiting:    sstr = f"Waiting: {st.waiting.reason or ''}"
        elif st.terminated: sstr = f"Terminated (exit={st.terminated.exit_code})"
        else:               sstr = "Unknown"
        containers.append({"name": cs.name, "image": cs.image,
                            "ready": cs.ready, "restarts": cs.restart_count, "state": sstr})
    resources = []
    for c in (spec.containers or []):
        req = (c.resources.requests or {}) if c.resources else {}
        lim = (c.resources.limits   or {}) if c.resources else {}
        resources.append({
            "name":       c.name,
            "req_cpu":    req.get("cpu",    "⚠ not set"),
            "req_memory": req.get("memory", "⚠ not set"),
            "lim_cpu":    lim.get("cpu",    "⚠ not set"),
            "lim_memory": lim.get("memory", "⚠ not set"),
            "warn":       not req or not lim,
        })
    return {
        "name": meta.name, "namespace": meta.namespace, "phase": phase,
        "node": spec.node_name or "—", "pod_ip": status.pod_ip or "—",
        "age":  age(meta.creation_timestamp), "ready": f"{ready}/{total}",
        "labels": dict(list((meta.labels or {}).items())[:8]),
        "containers": containers, "resources": resources,
        "conditions": [{"type": c.type, "status": c.status, "reason": c.reason or ""}
                        for c in (status.conditions or [])],
        "health": "running" if phase == "Running" else "pending" if phase == "Pending" else "failed",
    }


def serialize_deployment(d):
    meta, spec, status = d.metadata, d.spec, d.status
    desired = spec.replicas or 0
    ready   = status.ready_replicas or 0
    containers = []
    for c in (spec.template.spec.containers or []):
        req = (c.resources.requests or {}) if c.resources else {}
        lim = (c.resources.limits   or {}) if c.resources else {}
        containers.append({
            "name": c.name, "image": c.image,
            "req_cpu":    req.get("cpu",    "⚠ not set"),
            "req_memory": req.get("memory", "⚠ not set"),
            "lim_cpu":    lim.get("cpu",    "⚠ not set"),
            "lim_memory": lim.get("memory", "⚠ not set"),
            "warn": not req or not lim,
        })
    return {
        "name": meta.name, "namespace": meta.namespace,
        "age":  age(meta.creation_timestamp),
        "desired": desired, "ready": ready,
        "available": status.available_replicas or 0,
        "updated":   status.updated_replicas   or 0,
        "strategy":  spec.strategy.type if spec.strategy else "—",
        "containers": containers,
        "conditions": [{"type": c.type, "status": c.status, "message": c.message or ""}
                        for c in (status.conditions or [])],
        "health": "healthy" if ready == desired and desired > 0
                  else "degraded" if ready > 0 else "unhealthy",
    }


def serialize_statefulset(s):
    meta, spec, status = s.metadata, s.spec, s.status
    desired = spec.replicas or 0
    ready   = status.ready_replicas or 0
    vclaims = []
    for vct in (spec.volume_claim_templates or []):
        vclaims.append({
            "name":    vct.metadata.name,
            "storage": (vct.spec.resources.requests or {}).get("storage", "—"),
            "class":   vct.spec.storage_class_name or "default",
        })
    return {
        "name": meta.name, "namespace": meta.namespace,
        "age": age(meta.creation_timestamp),
        "desired": desired, "ready": ready, "service": spec.service_name,
        "containers": [{"name": c.name, "image": c.image}
                        for c in (spec.template.spec.containers or [])],
        "vclaims": vclaims,
        "health": "healthy" if ready == desired and desired > 0
                  else "degraded" if ready > 0 else "unhealthy",
    }


def serialize_service(s):
    meta, spec = s.metadata, s.spec
    ports = []
    for p in (spec.ports or []):
        tp = p.target_port if isinstance(p.target_port, str) else str(p.target_port)
        ports.append({"name": p.name or "—", "protocol": p.protocol,
                       "port": p.port, "target": tp})
    ext_ips = []
    if spec.type == "LoadBalancer" and s.status.load_balancer and s.status.load_balancer.ingress:
        ext_ips = [i.ip or i.hostname for i in s.status.load_balancer.ingress]
    return {
        "name": meta.name, "namespace": meta.namespace,
        "age": age(meta.creation_timestamp),
        "type": spec.type, "cluster_ip": spec.cluster_ip,
        "ext_ips": ext_ips, "ports": ports, "selector": spec.selector or {},
    }


def serialize_configmap(cm):
    data = cm.data or {}
    return {
        "name": cm.metadata.name, "namespace": cm.metadata.namespace,
        "age":  age(cm.metadata.creation_timestamp),
        "keys": list(data.keys()),
        "data": {k: v[:3000] for k, v in data.items()},
    }


def serialize_secret(s):
    data = s.data or {}
    return {
        "name": s.metadata.name, "namespace": s.metadata.namespace,
        "age":  age(s.metadata.creation_timestamp), "type": s.type,
        "keys": [{"name": k, "size": len(v) if v else 0} for k, v in data.items()],
    }


def serialize_ingress(ing):
    meta, spec = ing.metadata, ing.spec
    rules = []
    for rule in (spec.rules or []):
        paths = []
        if rule.http:
            for p in rule.http.paths:
                svc = p.backend.service
                paths.append({"path": p.path or "/", "service": svc.name, "port": svc.port.number})
        rules.append({"host": rule.host or "*", "paths": paths})
    return {
        "name": meta.name, "namespace": meta.namespace,
        "age":   age(meta.creation_timestamp),
        "class": spec.ingress_class_name or "—", "rules": rules,
        "tls":   [{"hosts": t.hosts or [], "secret": t.secret_name} for t in (spec.tls or [])],
    }


def serialize_pvc(pvc):
    meta, spec, status = pvc.metadata, pvc.spec, pvc.status
    return {
        "name": meta.name, "namespace": meta.namespace,
        "age":           age(meta.creation_timestamp),
        "status":        status.phase or "Unknown",
        "volume":        spec.volume_name or "—",
        "capacity":      (status.capacity or {}).get("storage", "—"),
        "storage_class": spec.storage_class_name or "—",
        "access_modes":  spec.access_modes or [],
        "request":       (spec.resources.requests or {}).get("storage", "—")
                          if spec.resources else "—",
        "health": "bound" if status.phase == "Bound"
                  else "pending" if status.phase == "Pending" else "lost",
    }


def serialize_pv(pv):
    meta, spec, status = pv.metadata, pv.spec, pv.status
    claim = "—"
    if spec.claim_ref:
        claim = f"{spec.claim_ref.namespace}/{spec.claim_ref.name}"
    source_type = "—"
    for src in ["host_path", "nfs", "aws_elastic_block_store", "gce_persistent_disk",
                "azure_disk", "csi", "local", "fc", "iscsi"]:
        if getattr(spec, src, None):
            source_type = src.replace("_", " ").title()
            break
    return {
        "name": meta.name, "age": age(meta.creation_timestamp),
        "status":         status.phase or "Unknown",
        "capacity":       (spec.capacity or {}).get("storage", "—"),
        "access_modes":   spec.access_modes or [],
        "reclaim_policy": spec.persistent_volume_reclaim_policy or "—",
        "storage_class":  spec.storage_class_name or "—",
        "claim": claim, "source_type": source_type,
        "health": "bound"     if status.phase == "Bound"
                  else "available" if status.phase == "Available" else "released",
    }


def serialize_event(e):
    return {
        "type":    e.type    or "Normal",
        "reason":  e.reason  or "",
        "message": e.message or "",
        "age":     age(best_ts(e)),
        "count":   e.count   or 1,
    }


def serialize_event_full(e):
    obj     = e.involved_object
    obj_str = f"{obj.kind}/{obj.name}" if obj else "—"
    return {
        "name":            e.metadata.name,
        "namespace":       e.metadata.namespace,
        "type":            e.type    or "Normal",
        "reason":          e.reason  or "",
        "message":         (e.message or "").replace("\n", " ")[:200],
        "involved_object": obj_str,
        "count":           e.count   or 1,
        "age":             age(best_ts(e)),
        "first_seen":      age(e.first_timestamp or e.metadata.creation_timestamp),
    }


def serialize_namespace_summary(k8s, namespace: str):
    pods = k8s.get_pods()
    return {
        "namespace": namespace,
        "pods": {
            "total":   len(pods),
            "running": sum(1 for p in pods if (p.status.phase or "") == "Running"),
            "pending": sum(1 for p in pods if (p.status.phase or "") == "Pending"),
            "failed":  sum(1 for p in pods if (p.status.phase or "") == "Failed"),
        },
        "deployments":  len(k8s.get_deployments()),
        "statefulsets": len(k8s.get_statefulsets()),
        "services":     len(k8s.get_services()),
        "configmaps":   len(k8s.get_configmaps()),
        "secrets":      len(k8s.get_secrets()),
        "ingresses":    len(k8s.get_ingresses()),
        "pvcs":         len(k8s.get_pvcs()),
        "pvs":          len(k8s.get_pvs()),
    }


def serialize_all_ns_summary(k8s):
    all_pods = k8s.get_all_pods()
    all_deps = k8s.get_all_deployments()
    all_stss = k8s.get_all_statefulsets()
    all_svcs = k8s.get_all_services()
    all_pvcs = k8s.get_all_pvcs()
    all_cms  = k8s.get_all_configmaps()
    all_secs = k8s.get_all_secrets()
    all_ings = k8s.get_all_ingresses()
    all_pvs  = k8s.get_pvs()
    nss = {}

    def ns_entry(n):
        if n not in nss:
            nss[n] = {"namespace": n, "pods": 0, "pods_running": 0,
                      "deployments": 0, "statefulsets": 0, "services": 0,
                      "pvcs": 0, "configmaps": 0, "secrets": 0, "ingresses": 0}
        return nss[n]

    for p in all_pods:
        e = ns_entry(p.metadata.namespace)
        e["pods"] += 1
        if (p.status.phase or "") == "Running":
            e["pods_running"] += 1

    for lst, key in [(all_deps,"deployments"),(all_stss,"statefulsets"),
                     (all_svcs,"services"),   (all_pvcs,"pvcs"),
                     (all_cms,"configmaps"),  (all_secs,"secrets"),
                     (all_ings,"ingresses")]:
        for item in lst:
            ns_entry(item.metadata.namespace)[key] += 1

    return {
        "namespace": "__all__",
        "breakdown": sorted(nss.values(), key=lambda x: x["namespace"]),
        "pods":         {"total":   len(all_pods),
                          "running": sum(1 for p in all_pods if (p.status.phase or "") == "Running"),
                          "pending": sum(1 for p in all_pods if (p.status.phase or "") == "Pending"),
                          "failed":  sum(1 for p in all_pods if (p.status.phase or "") == "Failed")},
        "deployments":  len(all_deps),
        "statefulsets": len(all_stss),
        "services":     len(all_svcs),
        "pvcs":         len(all_pvcs),
        "pvs":          len(all_pvs),
        "configmaps":   len(all_cms),
        "secrets":      len(all_secs),
        "ingresses":    len(all_ings),
    }
