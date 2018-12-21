
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
Get minikube IP by running `minikube ip`

Since the demos expose the services over `NodePort`

Get the service port by,
```kubectl get services```

Applications endpoint would be <minikube-ip>:servicePort

## OR,

`minikube service <service-name> --url`