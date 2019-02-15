
## Monitor the kubernetes cluster

### 1. Change active namespace
`kubectl config set-context $(kubectl config current-context) --namespace=monitoring`
### 2. Run cluster role
### 3. Run Config map
### 4. Run Deployment and Service

# OR

## Run `kubectl create -f <directory>`