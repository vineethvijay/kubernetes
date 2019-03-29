Deploy prometheus

```
kubectl create -f monitoring-namespace.yaml
kubectl create -f prometheus-config.yaml
kubectl create -f prometheus-deployment.yaml
kubectl create -f prometheus-service.yaml
```

Show prometheus, `minikube service --namespace=monitoring prometheus`


Deploy grafana
```
kubectl create -f grafana-deployment.yaml
kubectl create -f grafana-service.yaml
```

Show grafana,
`minikube service --namespace=monitoring grafana`

Deploy node-exporter,

`kubectl create -f node-exporter-daemonset.yml`