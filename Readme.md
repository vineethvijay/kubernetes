
# Minikube kubernetes examples

## Environment

```
Machine:  macOS High Sierra
minikube version: v0.31.0
Namespace : default
```

### Installation
Minikube (+ kubectl) Installation : https://kubernetes.io/docs/tasks/tools/install-minikube/

Start Minikube with resource limits,

`minikube start --cpus 4 --memory 8192`


### Running Applications
All sample projects can be run using,

`kubectl create -f <directory>`

Cleanup,

`kubectl delete -f <directory>`

List pods,

`kubectl get pods`

Describe a pod,

`kubectl describe pod <pod-name>`

Get pod (container-level) logs,

`kubectl logs -f <pod-name>`

List services,

`kubectl get services`



### Accessing the applications

Endpoint would be (as we use service type `NodePort` )

`echo $(minikube ip):$(kubectl get service/<service-name> -o jsonpath="{.spec.ports[*].nodePort}")`

## OR,

`minikube service <service-name> --url`