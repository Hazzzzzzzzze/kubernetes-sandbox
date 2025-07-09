# Kubernetes: Learning the Hard Way

Welcome! This project is for learning Kubernetes (k8s) by doing everything manually. Below you'll find essential concepts and the most useful `kubectl` commands for hands-on learning.

## Key Kubernetes Concepts

- **Cluster**: The whole Kubernetes system, made up of nodes.
- **Node**: A machine (virtual or physical) that runs your application workloads. A cluster has at least one node (often many).
- **Pod**: The smallest deployable unit in Kubernetes. A pod can hold one or more containers (usually one), and runs on a node.
- **Deployment**: Manages pods and ensures the right number are running at all times.
- **Service**: Exposes your pods to the network (internal or external), acting as a load balancer or gateway.

## Step-by-Step: Recreate and Test Your Cluster

1. **Create a new cluster:**
   ```sh
   k3d cluster create cluster-1 -p "8081:80@loadbalancer"
   ```
   > Uses your custom kind config to set up the cluster.

2. **Install the metrics server (for HPA):**
   ```sh
   kubectl apply -f metrics-server.yaml
   ```
   > Enables resource metrics required for autoscaling.

3. **Deploy your app and service:**
   ```sh
   kubectl apply -f deployment.yaml
   ```
   > Deploys the sample-app Deployment and Service.

4. **Enable autoscaling with HPA:**
   ```sh
   kubectl apply -f hpa.yaml
   ```
   > Sets up the Horizontal Pod Autoscaler for your app.

5. **(Optional) Deploy the load generator:**
   ```sh
   kubectl apply -f load-generator.yaml
   ```
   > Creates a pod that continuously sends requests to your app to trigger scaling.

6. **(Optional) Deploy the Kubernetes Dashboard:**
   ```sh
   kubectl apply -f kubernetes-dashboard.yaml
   ```
   > Installs a web UI to view and manage your cluster.
   ```sh
   kubectl proxy
   ```
   ```
   kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard 8001:443
   ```
   > Starts a proxy server to access the dashboard.
   ```sh
   kubectl apply -f dashboard-admin.yaml
   ```
   > Grants admin permissions to the dashboard.
---
7. **(Optional) Deploy the Ingress:**
   ```sh
   kubectl apply -f ingress.yaml
   ```
   > Creates an Ingress resource to expose your app.

## Useful kubectl Commands

- `kubectl get nodes` — List all nodes in your cluster
- `kubectl get pods` — List all pods in your cluster
- `kubectl get deployments` — List all deployments
- `kubectl get services` — List all services
- `kubectl get hpa` — List all Horizontal Pod Autoscalers
- `kubectl describe pod <pod-name>` — Detailed info about a pod
- `kubectl logs <pod-name>` — Show logs from a pod
- `kubectl exec -it <pod-name> -- /bin/sh` — Open a shell inside a running pod
- `kubectl get all` — List all resources (pods, services, deployments, etc.)
- `kubectl delete -f <file.yaml>` — Delete resources defined in a YAML file
- `kubectl delete pod <pod-name>` — Delete a specific pod
---

## Load Generator
- `kubectl apply -f load-generator.yaml` — Apply the load generator pod
- `kubectl exec -it load-generator -- /bin/sh` — Open a shell inside the load generator pod
- `kubectl delete -f load-generator.yaml` — Delete the load generator pod

## Clean Up
- `kind delete cluster` — Delete the entire cluster and all resources

---
Happy learning! Add more commands or notes here as you progress.

## Tips
- Always check the status of your resources with `kubectl get ...`.
- Use `kubectl describe ...` for detailed troubleshooting.
- Clean up with `kubectl delete ...` to avoid resource clutter.

## Dashboard
- Access the dashboard at `https://localhost:8001`
- Use the token from `kubectl -n kubernetes-dashboard create token admin-user`
