
Build the docker image ,
(or you can upload the image to a public repository and change the image in deployment.yml)


`docker build . -t python-app`

Note : make sure you use the minikube docker environment,
If not, run

`eval $(minikube docker-env)`


## Run `kubectl create -f <directory>`