# kubectl — Basic Commands & Usage Examples

A concise reference for common kubectl commands and typical workflows.

## Prerequisites
- kubectl installed and in PATH
- Access to a Kubernetes cluster and a configured kubeconfig (`~/.kube/config`)
- Basic familiarity with Kubernetes resources (Pod, Deployment, Service, Namespace)

## Quick reference
- Show cluster info:
```bash
kubectl cluster-info
```
- Show config and contexts:
```bash
kubectl config view
kubectl config current-context
kubectl config get-contexts
kubectl config use-context my-cluster
```
- Set namespace for a single command:
```bash
kubectl get pods -n my-namespace
```
- Set default namespace for current context:
```bash
kubectl config set-context --current --namespace=my-namespace
```

## Inspecting resources
- List resources:
```bash
kubectl get pods
kubectl get deployments
kubectl get svc
kubectl get all               # all default resource types
kubectl get pods -o wide      # more details
kubectl get pods -o yaml      # full resource YAML
```
- Describe resource (human-readable events & details):
```bash
kubectl describe pod my-pod
```
- Show resource definition:
```bash
kubectl get deployment my-deploy -o yaml
```

## Creating, updating and deleting
- Create from file or stdin:
```bash
kubectl apply -f manifest.yaml   # declarative (creates or updates)
kubectl create -f manifest.yaml  # imperative create
```
- Imperative create common resources:
```bash
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --target-port=80 --type=ClusterIP
```
- Update using apply after changing manifest:
```bash
kubectl apply -f deployment.yaml
```
- Delete resources:
```bash
kubectl delete -f manifest.yaml
kubectl delete pod my-pod
kubectl delete deployment my-deploy
```

## Debugging and runtime ops
- View logs:
```bash
kubectl logs my-pod                 # single-container pod
kubectl logs my-pod -c container    # multi-container pod
kubectl logs -f my-pod              # follow logs
kubectl logs deployment/my-deploy   # logs of pods in deployment (best-effort)
```
- Exec into a running container:
```bash
kubectl exec -it my-pod -- /bin/sh
kubectl exec -it my-pod -c container -- /bin/bash
```
- Port-forward local port to pod/service:
```bash
kubectl port-forward svc/my-service 8080:80
kubectl port-forward pod/my-pod 8080:80
```
- Copy files to/from a pod:
```bash
kubectl cp localfile my-pod:/tmp/remote
kubectl cp my-pod:/var/log/app.log ./app.log
```

## Scaling and rolling updates
- Scale a deployment:
```bash
kubectl scale deployment my-deploy --replicas=5
```
- Rolling restart:
```bash
kubectl rollout restart deployment/my-deploy
kubectl rollout status deployment/my-deploy
kubectl rollout history deployment/my-deploy
```
- Undo rollout:
```bash
kubectl rollout undo deployment/my-deploy
```

## Labels, selectors and field selectors
- Add or update labels:
```bash
kubectl label pod my-pod env=prod --overwrite
```
- Select by label:
```bash
kubectl get pods -l app=nginx
kubectl delete pods -l env=staging
```
- Use field selector (e.g., by status or node):
```bash
kubectl get pods --field-selector=status.phase=Failed
kubectl get pods --field-selector=spec.nodeName=my-node
```

## ConfigMaps and Secrets
- Create from literal or file:
```bash
kubectl create configmap my-config --from-literal=key=value
kubectl create secret generic my-secret --from-literal=password=secret
kubectl create configmap app-config --from-file=./config/
```
- Inspect:
```bash
kubectl get configmap my-config -o yaml
kubectl describe secret my-secret
kubectl get secret my-secret -o jsonpath="{.data.password}" | base64 --decode
```

## Namespaces
- Create and use:
```bash
kubectl create namespace dev
kubectl get pods -n dev
kubectl config set-context --current --namespace=dev
```
- Delete namespace:
```bash
kubectl delete namespace dev
```

## Resource usage & metrics
- Node and pod metrics (requires metrics-server):
```bash
kubectl top node
kubectl top pod
```

## Helpful utilities
- Explain resource fields:
```bash
kubectl explain deployment.spec.template.spec.containers
```
- Autocomplete (bash):
```bash
source <(kubectl completion bash)
# Add to ~/.bashrc for persistent completion
```
- Dry-run to preview changes:
```bash
kubectl apply -f manifest.yaml --dry-run=client -o yaml
```
- Patch a resource (json merge patch or strategic):
```bash
kubectl patch deployment my-deploy -p '{"spec":{"replicas":3}}'
```

## Examples: typical workflows
- Deploy a simple nginx app:
```bash
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=ClusterIP
kubectl get pods
kubectl get svc
```
- Update image and rollout:
```bash
kubectl set image deployment/nginx nginx=nginx:1.21
kubectl rollout status deployment/nginx
```
- Debug failing pod:
```bash
kubectl describe pod my-pod
kubectl logs my-pod --previous
kubectl exec -it my-pod -- sh
```

## Tips
- Prefer declarative workflows (git + manifests) using kubectl apply.
- Use namespaces to isolate environments.
- Use labels and selectors for organization and bulk operations.
- Use kubectl --context and --kubeconfig to manage multiple clusters.

Further reading: kubectl official docs (`kubectl --help` and https://kubernetes.io/docs/reference/kubectl/)
