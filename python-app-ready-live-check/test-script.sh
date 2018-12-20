#!/usr/bin/env bash

#replace appname -- service/<appname>

while true
do
  curl $(minikube ip):$(kubectl get service/python-app -o jsonpath="{.spec.ports[*].nodePort}")
  echo ""
  sleep .5;
done