# K8s Multi-Cluster Analyzer

A lightweight, self-contained web dashboard for monitoring and managing multiple Kubernetes clusters from a browser. Works air-gapped.

---

## Architecture

```
k8s_analyzer.py   FastAPI application — all HTTP routes and CLI entry point
k8s_module.py     K8s client wrapper, serializers, cluster registry, 60s client cache
html_pages.py     Entire frontend as Python string constants (HTML + CSS + JS, ~1600 lines)
clusters.json     Auto-created on first cluster add; stores kubeconfig content (not file paths)
requirements.txt  Python package dependencies
```

The frontend is entirely server-rendered from Python strings — there is no build step, no npm, no bundler. Opening `http://server:port/` serves a single self-contained HTML page.

---

## Requirements

**Python 3.8+**

```
kubernetes>=28.1.0
fastapi>=0.110.0
uvicorn>=0.29.0
pyyaml>=6.0
python-multipart==0.0.22
```

Install:
```bash
pip install kubernetes fastapi uvicorn pyyaml python-multipart
```

---

## Running

```bash
# Default port 8080
python k8s_analyzer.py

# Custom port
python k8s_analyzer.py --port 9090
python k8s_analyzer.py -p 9090

# Custom clusters registry file
python k8s_analyzer.py --clusters-file /data/my-clusters.json

# Combined
python k8s_analyzer.py --port 9090 --clusters-file /data/clusters.json
```

On startup, the terminal prints the server IP and URL:
```
⎈  K8s Multi-Cluster Analyzer
   http://192.168.1.10:9090  |  http://localhost:9090
   Ctrl+C to stop
```

---

## CLI — Test Connectivity Without Starting the Server

Use `--test` mode to verify kubeconfig connectivity from the command line, without launching the web server:

```bash
python k8s_analyzer.py --test --kubeconfig /etc/kubernetes/admin.conf
python k8s_analyzer.py --test -k ~/.kube/config -n openwebui
python k8s_analyzer.py -t -k /etc/k3s/k3s.yaml --namespace kube-system
```

Output example:
```
⎈  Testing /etc/kubernetes/admin.conf...
✓  v1.28.4  |  7 namespaces
✓  3 pods in 'default'
✅  OK
```

---

## Adding a Cluster

1. Open the UI → click **⚙️ Clusters** in the sidebar
2. Click **➕ Add New Cluster**
3. Enter a display name (e.g. `production`, `dev-cluster`)
4. Upload your kubeconfig file (supports `kubeconfig`, `admin.conf`, `k3s.yaml`)
5. Optionally add a description
6. Click **Add & Test Connection**

The kubeconfig YAML content is stored directly in `clusters.json` under the `kubeconfig_data` key. No file paths. No symlinks. The file can be copied between machines.

---

## UI Navigation

```
🏠 Cluster Overview (default page)
   ├── Cards render instantly from registry (no K8s calls on page load)
   ├── Status checks fire in parallel per-cluster (async)
   ├── Deep stats (nodes/pods/deployments) load after status confirms connected
   ├── [Open Dashboard] → Namespace Dashboard, defaults to ⬡ All Namespaces
   └── [🖥️ Nodes] → full node table, click row for detail panel

⚙️ Cluster Management
   ├── Per-cluster cards with Test / Remove buttons
   └── Collapsible ➕ Add New Cluster form with drag-and-drop kubeconfig upload

📊 Namespace Dashboard
   ├── Namespace selector (dropdown): individual namespace or ⬡ All Namespaces
   │
   ├── ⬡ All Namespaces view:
   │    ├── Stat row: running/pending/failed pods, namespace count, deployments, services
   │    ├── Per-namespace breakdown table (pods, running, deployments, STS, services, PVCs, secrets)
   │    │    └── click any row → drill into that namespace
   │    └── Resource cards: browse all resources across namespaces
   │
   └── Single Namespace view:
        └── Resource count cards for all resource types → click to open resource list

Resource List pages (Pods, Deployments, StatefulSets, Services, PVCs, PVs,
                     ConfigMaps, Secrets, Ingresses, Events)
   ├── Pods list: 🟢 auto-refreshes every 2 seconds, scroll position preserved
   ├── All Namespaces mode adds a Namespace column with cyan badge
   ├── 3-dot (⋯) action menu per row:
   │    ├── Pods:         🗑️ Delete Pod
   │    ├── Deployments:  ⟳ Rollout Restart · 🗑️ Delete
   │    └── StatefulSets: ⟳ Rollout Restart · 🗑️ Delete
   └── Click any row → Detail view

Detail View
   ├── Pod detail:
   │    ├── ↻ Refresh (re-fetches live pod data)
   │    ├── Node, IP, age, ready count, labels
   │    ├── Container info: image, state, restarts, CPU/memory requests & limits (⚠ if unset)
   │    ├── Conditions (PodReady, Initialized, etc.)
   │    ├── Events section with ↻ Refresh (always fetches live, bypasses cache)
   │    └── Logs: Show/Hide toggle · tail selector (100/200/500/1000 lines) ·
   │             Errors only filter · text filter · ANSI codes stripped
   │
   ├── Deployment / StatefulSet detail:
   │    ├── ⟳ Rollout Restart button (patches restartedAt annotation)
   │    ├── Replica status, strategy, container images
   │    ├── Resource requests/limits with ⚠ warnings for unset limits
   │    ├── Conditions
   │    └── Last 5 events
   │
   └── Other resources: full field display appropriate to type
```

---

## Actions

All mutating actions show toast notifications (✅ success, ❌ error, ⏳ in-progress).

| Action | How | Behaviour |
|--------|-----|-----------|
| **Delete Pod** | 3-dot menu in pods list | Confirms → deletes → immediately removes from list → re-fetches after 2s |
| **Delete Deployment** | 3-dot menu in deployments list | Confirms → deletes → removes from list immediately |
| **Delete StatefulSet** | 3-dot menu in statefulsets list | Confirms → deletes → removes from list immediately |
| **Rollout Restart Deployment** | 3-dot menu or detail button | Patches `kubectl.kubernetes.io/restartedAt` annotation — triggers rolling restart |
| **Rollout Restart StatefulSet** | 3-dot menu or detail button | Same annotation patch approach |

---

## Refresh Button (↻)

The topbar ↻ Refresh button is context-aware — it refreshes the correct data for whatever page you are currently viewing:

| Current page | What refreshes |
|---|---|
| Cluster Overview | Re-checks all cluster statuses |
| Cluster Management | Reloads cluster cards |
| Nodes | Reloads node list for current cluster |
| Namespace Dashboard | Reloads all resource counts |
| Resource list | Reloads namespace data + re-renders list |
| Pod detail | Reloads pod data + events + logs (if open) |
| Other detail | Reloads namespace data + re-renders detail |

---

## API Reference

All endpoints return JSON. The `{cluster}` parameter is the display name set when adding the cluster.

### Cluster Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/clusters` | List clusters from registry — **instant, zero K8s calls** |
| `GET` | `/api/clusters/{name}/status` | Live connectivity check for one cluster |
| `POST` | `/api/clusters` | Register a cluster `{name, kubeconfig_data, description}` |
| `DELETE` | `/api/clusters/{name}` | Remove cluster from registry |
| `POST` | `/api/clusters/upload` | Upload kubeconfig file → `{kubeconfig_data, contexts, filename}` |
| `POST` | `/api/clusters/{name}/test` | Test connectivity, return version + namespace count |

### Cluster-Level

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/{cluster}/namespaces` | List all namespaces (sorted) |
| `GET` | `/api/{cluster}/overview` | Nodes, pods, deployments counts + health summary |
| `GET` | `/api/{cluster}/nodes` | Full node list with CPU, memory, taints, conditions, labels |

### All-Namespace Queries (`/__all__/`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/{cluster}/__all__/summary` | Totals + per-namespace breakdown array |
| `GET` | `/api/{cluster}/__all__/pods` | All pods across all namespaces |
| `GET` | `/api/{cluster}/__all__/deployments` | All deployments |
| `GET` | `/api/{cluster}/__all__/statefulsets` | All StatefulSets |
| `GET` | `/api/{cluster}/__all__/services` | All Services |
| `GET` | `/api/{cluster}/__all__/configmaps` | All ConfigMaps |
| `GET` | `/api/{cluster}/__all__/secrets` | All Secrets (keys only) |
| `GET` | `/api/{cluster}/__all__/pvcs` | All PersistentVolumeClaims |
| `GET` | `/api/{cluster}/__all__/ingresses` | All Ingresses |
| `GET` | `/api/{cluster}/__all__/events` | All events, sorted newest-first |

### Namespace-Level

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/{cluster}/{ns}/summary` | Resource counts for namespace |
| `GET` | `/api/{cluster}/{ns}/pods` | Pod list with container states and resource info |
| `GET` | `/api/{cluster}/{ns}/pods/{pod}/logs` | Pod logs · query param `?tail=200` |
| `GET` | `/api/{cluster}/{ns}/pods/{pod}/events` | Pod events — **always fresh client, no cache** |
| `GET` | `/api/{cluster}/{ns}/deployments` | Deployments + last 5 events each |
| `GET` | `/api/{cluster}/{ns}/statefulsets` | StatefulSets + last 5 events each |
| `GET` | `/api/{cluster}/{ns}/services` | Services with port mappings |
| `GET` | `/api/{cluster}/{ns}/configmaps` | ConfigMaps with data (truncated at 3000 chars/key) |
| `GET` | `/api/{cluster}/{ns}/secrets` | Secrets — **key names and byte sizes only, values never returned** |
| `GET` | `/api/{cluster}/{ns}/ingresses` | Ingresses with rules and TLS config |
| `GET` | `/api/{cluster}/{ns}/pvcs` | PersistentVolumeClaims |
| `GET` | `/api/{cluster}/{ns}/pvs` | PersistentVolumes (cluster-wide, namespace param ignored) |
| `GET` | `/api/{cluster}/{ns}/events` | All namespace events, newest-first |

### Actions

| Method | Endpoint | Description |
|--------|----------|-------------|
| `DELETE` | `/api/{cluster}/{ns}/pods/{pod}` | Delete pod (controller will recreate if managed) |
| `DELETE` | `/api/{cluster}/{ns}/deployments/{name}` | Delete deployment and its pods |
| `DELETE` | `/api/{cluster}/{ns}/statefulsets/{name}` | Delete StatefulSet and its pods |
| `POST` | `/api/{cluster}/{ns}/pods/{pod}/restart` | Restart pod by deletion |
| `POST` | `/api/{cluster}/{ns}/deployments/{name}/restart` | Rollout restart via annotation patch |
| `POST` | `/api/{cluster}/{ns}/statefulsets/{name}/restart` | Rollout restart via annotation patch |

---

## clusters.json

Clusters are stored as a JSON array. Each entry holds the full kubeconfig YAML as a string — no file references.

```json
[
  {
    "name": "production",
    "kubeconfig_data": "apiVersion: v1\nclusters:\n- cluster:\n    server: https://...\n  name: prod\n...",
    "description": "Production cluster DC1"
  },
  {
    "name": "staging",
    "kubeconfig_data": "apiVersion: v1\n...",
    "description": ""
  }
]
```

This file is created automatically when the first cluster is added. It is safe to copy to another machine — no absolute paths are stored anywhere.

> **Migration note:** Older versions used a `"kubeconfig"` field with a file path. That format is no longer supported. Re-add clusters through the UI if you have an old `clusters.json`.

---

## Caching

K8s API client objects are cached in memory with a **60-second TTL** keyed by `cluster::namespace`. After 60 seconds the client is recreated on next use. This balances connection overhead against data freshness.

**Pod events bypass the cache entirely** — a fresh `K8sClient` is created on every `/pods/{pod}/events` request to ensure event data is never stale.

The in-memory cache is cleared when a cluster is removed.

---

## Security Notes

- Secret values are **never** returned by any endpoint — only key names and byte sizes
- ConfigMap values are truncated to 3000 characters per key
- The `kubeconfig_data` field is **never** included in `GET /api/clusters` responses — only name, description, and status are returned
- No authentication layer is built in — use a reverse proxy or network controls to restrict access

---

## Known Limitations

- Log streaming is not supported — use the tail selector (100 / 200 / 500 / 1000 lines) and manual refresh
- PersistentVolumes are always cluster-wide regardless of selected namespace
- Pod restart (from detail view) works by deletion — only effective for pods managed by a controller (Deployment, StatefulSet, DaemonSet, etc.)
- Multi-container pod logs show the first container only (Kubernetes default when no container name is specified)
- `NetworkingV1Api` ingresses require Kubernetes 1.19+; older clusters will silently return empty ingress lists