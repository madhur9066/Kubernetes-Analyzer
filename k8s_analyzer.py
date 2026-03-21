#!/usr/bin/env python3
"""
k8s_analyzer.py — FastAPI routes.
Kubeconfig stored as YAML string in clusters.json — no file paths.
Usage: python k8s_analyzer.py --port 9090
"""

import argparse
import os
import socket

try:
    import uvicorn
    from fastapi import FastAPI, HTTPException, UploadFile, File
    from fastapi.responses import HTMLResponse
    from fastapi.middleware.cors import CORSMiddleware
    from pydantic import BaseModel
    FASTAPI_OK = True
except ImportError:
    FASTAPI_OK = False

from k8s_module import (
    K8S_AVAILABLE, K8sClient, CLUSTERS_FILE,
    load_clusters, save_clusters, clear_cluster_cache, get_client,
    serialize_node, serialize_pod, serialize_deployment, serialize_statefulset,
    serialize_service, serialize_configmap, serialize_secret,
    serialize_ingress, serialize_pvc, serialize_pv,
    serialize_event, serialize_event_full,
    serialize_namespace_summary, serialize_all_ns_summary,
)
from html_pages import get_page


def get_server_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]; s.close()
        return ip
    except Exception:
        return "localhost"


def create_app(clusters_file=CLUSTERS_FILE):
    app = FastAPI(title="K8s Analyzer")
    app.add_middleware(CORSMiddleware, allow_origins=["*"],
                       allow_methods=["*"], allow_headers=["*"])

    def k8s(cluster, ns):
        try:
            return get_client(cluster, ns, clusters_file)
        except ValueError as e:
            raise HTTPException(404, str(e))
        except Exception as e:
            raise HTTPException(500, str(e))

    def get_kc(name):
        clusters = load_clusters(clusters_file)
        cl = next((c for c in clusters if c["name"] == name), None)
        if not cl:
            raise HTTPException(404, f"Cluster '{name}' not found")
        kc = cl.get("kubeconfig_data", "")
        if not kc:
            raise HTTPException(400, f"Cluster '{name}' has no kubeconfig — please re-add it.")
        return kc

    class ClusterAdd(BaseModel):
        name:            str
        kubeconfig_data: str
        description:     str = ""

    # ════════════ Cluster management ════════════

    @app.get("/api/clusters")
    def api_list_clusters():
        """Instant — reads clusters.json only, zero K8s calls."""
        result = []
        for c in load_clusters(clusters_file):
            entry = {"name": c["name"], "description": c.get("description", ""), "status": "unknown"}
            if not c.get("kubeconfig_data", ""):
                entry["status"] = "error"
                entry["error"]  = "No kubeconfig — please re-add this cluster."
            result.append(entry)
        return result

    @app.get("/api/clusters/{name}/status")
    def api_cluster_status(name: str):
        """Live check for ONE cluster — called async from UI."""
        try:
            cli = K8sClient(get_kc(name), "default")
            return {
                "name": name, "status": "connected",
                "version":    cli.get_server_version(),
                "namespaces": len(cli.get_namespaces()),
                "cluster":    cli.get_cluster_name(),
            }
        except HTTPException:
            raise
        except Exception as e:
            return {"name": name, "status": "error", "error": str(e)}

    @app.post("/api/clusters")
    def api_add_cluster(body: ClusterAdd):
        if not body.kubeconfig_data.strip():
            raise HTTPException(400, "kubeconfig_data is empty")
        try:
            cli     = K8sClient(body.kubeconfig_data, "default")
            version = cli.get_server_version()
            cname   = cli.get_cluster_name()
        except Exception as e:
            raise HTTPException(400, f"Cannot connect: {e}")
        clusters = load_clusters(clusters_file)
        if any(c["name"] == body.name for c in clusters):
            raise HTTPException(400, f"Name '{body.name}' already exists")
        clusters.append({"name": body.name, "kubeconfig_data": body.kubeconfig_data,
                          "description": body.description})
        save_clusters(clusters, clusters_file)
        return {"ok": True, "version": version, "cluster": cname}

    @app.delete("/api/clusters/{name}")
    def api_delete_cluster(name: str):
        clusters = [c for c in load_clusters(clusters_file) if c["name"] != name]
        save_clusters(clusters, clusters_file)
        clear_cluster_cache(name)
        return {"ok": True}

    @app.post("/api/clusters/upload")
    async def api_upload_kubeconfig(file: UploadFile = File(...)):
        contents = await file.read()
        try:
            import yaml
            parsed = yaml.safe_load(contents)
            if not isinstance(parsed, dict) or "clusters" not in parsed:
                raise HTTPException(400, "Not a valid kubeconfig file")
            contexts = [c.get("name", "") for c in parsed.get("contexts", [])]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(400, f"Invalid YAML: {e}")
        return {"kubeconfig_data": contents.decode("utf-8"),
                "filename": file.filename, "contexts": contexts}

    @app.post("/api/clusters/{name}/test")
    def api_test_cluster(name: str):
        try:
            cli = K8sClient(get_kc(name), "default")
            return {"ok": True, "version": cli.get_server_version(),
                    "cluster": cli.get_cluster_name(),
                    "namespaces": len(cli.get_namespaces())}
        except HTTPException:
            raise
        except Exception as e:
            return {"ok": False, "error": str(e)}

    # ════════════ Cluster-level ════════════

    @app.get("/api/{cluster}/namespaces")
    def api_namespaces(cluster: str):
        try:
            cli = K8sClient(get_kc(cluster), "default")
            return {"namespaces": cli.get_namespaces(), "cluster": cli.get_cluster_name()}
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/overview")
    def api_overview(cluster: str):
        try:
            return K8sClient(get_kc(cluster), "default").get_cluster_overview()
        except HTTPException:
            raise
        except Exception as e:
            return {"ok": False, "error": str(e)}

    @app.get("/api/{cluster}/nodes")
    def api_nodes(cluster: str):
        try:
            return [serialize_node(n) for n in K8sClient(get_kc(cluster), "default").get_nodes()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    # ════════════ All-namespace /__all__/ ════════════

    @app.get("/api/{cluster}/__all__/summary")
    def api_all_summary(cluster: str):
        try:
            return serialize_all_ns_summary(K8sClient(get_kc(cluster), "default"))
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/pods")
    def api_all_pods(cluster: str):
        try:
            return [serialize_pod(p) for p in K8sClient(get_kc(cluster), "default").get_all_pods()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/deployments")
    def api_all_deps(cluster: str):
        try:
            return [serialize_deployment(d) for d in K8sClient(get_kc(cluster), "default").get_all_deployments()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/statefulsets")
    def api_all_stss(cluster: str):
        try:
            return [serialize_statefulset(s) for s in K8sClient(get_kc(cluster), "default").get_all_statefulsets()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/services")
    def api_all_svcs(cluster: str):
        try:
            return [serialize_service(s) for s in K8sClient(get_kc(cluster), "default").get_all_services()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/configmaps")
    def api_all_cms(cluster: str):
        try:
            return [serialize_configmap(c) for c in K8sClient(get_kc(cluster), "default").get_all_configmaps()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/secrets")
    def api_all_secs(cluster: str):
        try:
            return [serialize_secret(s) for s in K8sClient(get_kc(cluster), "default").get_all_secrets()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/pvcs")
    def api_all_pvcs(cluster: str):
        try:
            return [serialize_pvc(p) for p in K8sClient(get_kc(cluster), "default").get_all_pvcs()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/ingresses")
    def api_all_ings(cluster: str):
        try:
            return [serialize_ingress(i) for i in K8sClient(get_kc(cluster), "default").get_all_ingresses()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/__all__/events")
    def api_all_events(cluster: str):
        try:
            return [serialize_event_full(e) for e in K8sClient(get_kc(cluster), "default").get_all_events()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    # ════════════ Namespace-level ════════════

    @app.get("/api/{cluster}/{namespace}/summary")
    def api_summary(cluster: str, namespace: str):
        try:
            return serialize_namespace_summary(k8s(cluster, namespace), namespace)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/pods")
    def api_pods(cluster: str, namespace: str):
        try:
            return [serialize_pod(p) for p in k8s(cluster, namespace).get_pods()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/pods/{pod}/logs")
    def api_logs(cluster: str, namespace: str, pod: str, tail: int = 200):
        try:
            return {"logs": k8s(cluster, namespace).get_pod_logs(pod, tail=tail)}
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/pods/{pod}/events")
    def api_pod_events(cluster: str, namespace: str, pod: str):
        try:
            # Always fresh client for events — never use cache
            cli = K8sClient(get_kc(cluster), namespace)
            return [serialize_event(e) for e in cli.get_events(pod)]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.delete("/api/{cluster}/{namespace}/pods/{pod}")
    def api_delete_pod(cluster: str, namespace: str, pod: str):
        try:
            return k8s(cluster, namespace).delete_pod(pod)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.delete("/api/{cluster}/{namespace}/deployments/{name}")
    def api_delete_deployment(cluster: str, namespace: str, name: str):
        try:
            return k8s(cluster, namespace).delete_deployment(name)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.delete("/api/{cluster}/{namespace}/statefulsets/{name}")
    def api_delete_statefulset(cluster: str, namespace: str, name: str):
        try:
            return k8s(cluster, namespace).delete_statefulset(name)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.post("/api/{cluster}/{namespace}/pods/{pod}/restart")
    def api_restart_pod(cluster: str, namespace: str, pod: str):
        try:
            return k8s(cluster, namespace).restart_pod(pod)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.post("/api/{cluster}/{namespace}/deployments/{name}/restart")
    def api_restart_deployment(cluster: str, namespace: str, name: str):
        try:
            return k8s(cluster, namespace).rollout_restart_deployment(name)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.post("/api/{cluster}/{namespace}/statefulsets/{name}/restart")
    def api_restart_statefulset(cluster: str, namespace: str, name: str):
        try:
            return k8s(cluster, namespace).rollout_restart_statefulset(name)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/deployments")
    def api_deps(cluster: str, namespace: str):
        try:
            cli = k8s(cluster, namespace)
            result = []
            for d in cli.get_deployments():
                sd = serialize_deployment(d)
                sd["events"] = [serialize_event(e) for e in cli.get_events(d.metadata.name)[:5]]
                result.append(sd)
            return result
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/statefulsets")
    def api_stss(cluster: str, namespace: str):
        try:
            cli = k8s(cluster, namespace)
            result = []
            for s in cli.get_statefulsets():
                ss = serialize_statefulset(s)
                ss["events"] = [serialize_event(e) for e in cli.get_events(s.metadata.name)[:5]]
                result.append(ss)
            return result
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/services")
    def api_svcs(cluster: str, namespace: str):
        try:
            return [serialize_service(s) for s in k8s(cluster, namespace).get_services()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/configmaps")
    def api_cms(cluster: str, namespace: str):
        try:
            return [serialize_configmap(c) for c in k8s(cluster, namespace).get_configmaps()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/secrets")
    def api_secs(cluster: str, namespace: str):
        try:
            return [serialize_secret(s) for s in k8s(cluster, namespace).get_secrets()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/ingresses")
    def api_ings(cluster: str, namespace: str):
        try:
            return [serialize_ingress(i) for i in k8s(cluster, namespace).get_ingresses()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/pvcs")
    def api_pvcs(cluster: str, namespace: str):
        try:
            return [serialize_pvc(p) for p in k8s(cluster, namespace).get_pvcs()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/pvs")
    def api_pvs(cluster: str, namespace: str):
        try:
            return [serialize_pv(p) for p in k8s(cluster, namespace).get_pvs()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/api/{cluster}/{namespace}/events")
    def api_events(cluster: str, namespace: str):
        try:
            return [serialize_event_full(e) for e in k8s(cluster, namespace).get_events()]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, str(e))

    @app.get("/", response_class=HTMLResponse)
    def index():
        return HTMLResponse(content=get_page())

    return app


def main():
    if not K8S_AVAILABLE:
        print("❌  Run: pip install kubernetes fastapi uvicorn pyyaml"); return

    parser = argparse.ArgumentParser(description="K8s Multi-Cluster Analyzer")
    parser.add_argument("--port",          "-p", type=int, default=8080)
    parser.add_argument("--clusters-file", "-f", default=CLUSTERS_FILE)
    parser.add_argument("--test",          "-t", action="store_true")
    parser.add_argument("--kubeconfig",    "-k", default=None)
    parser.add_argument("--namespace",     "-n", default="default")
    args = parser.parse_args()

    if args.test:
        if not args.kubeconfig: print("❌  --kubeconfig required"); return
        print(f"\n⎈  Testing {args.kubeconfig}...")
        try:
            kc  = open(args.kubeconfig).read()
            cli = K8sClient(kc, args.namespace)
            print(f"✓  {cli.get_server_version()}  |  {len(cli.get_namespaces())} namespaces")
            pods = cli.get_pods()
            print(f"✓  {len(pods)} pods in '{args.namespace}'")
            print("✅  OK\n")
        except Exception as e:
            print(f"✗  {e}\n")
        return

    if not FASTAPI_OK:
        print("❌  Run: pip install fastapi uvicorn"); return

    ip = get_server_ip()
    print(f"\n⎈  K8s Multi-Cluster Analyzer")
    print(f"   http://{ip}:{args.port}  |  http://localhost:{args.port}")
    print(f"   Ctrl+C to stop\n")
    uvicorn.run(create_app(clusters_file=args.clusters_file),
                host="0.0.0.0", port=args.port, log_level="warning")


if __name__ == "__main__":
    main()