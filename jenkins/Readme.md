### Following https://www.blazemeter.com/blog/how-to-setup-scalable-jenkins-on-top-of-a-kubernetes-cluster

Build the jenkins-master in minikube docker env
`eval $(minikube docker-env)`

Run `sudo chown -R 1000:1000 <mount-path>` in minikube node. login using `minikube ssh`

1.Configure Jenkins-->configure system--> cloud--> kubernetes with

a. URL: obtain by `kubectl cluster-info | grep master`
   Test connection
   
b. Jenkins url : Find `ip` from `kubectl describe pod jenkins-****` . Configure as http://<ip>:8080

Pod template 
    - pod label - <label>
    - image: https://hub.docker.com/r/jenkinsci/jnlp-slave/ , jenkins/jnlp-slave
    
2.Update master nodes executor to '0' for making sure builds use kubernetes pods executors

Sample pipeline jobs : https://github.com/jenkinsci/kubernetes-plugin

```
def label = "jenkins-slave-${UUID.randomUUID().toString()}"
podTemplate(label: label) {
    node(label) {
        stage('Run shell') {
            sh 'echo hello world'
            sh 'sleep 5'
        }
    }
}

```

Or run custom executor on pipeline

```
def label = "mypod-${UUID.randomUUID().toString()}"
podTemplate(label: label, yaml: """
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: some-label-value
spec:
  containers:
  - name: busybox
    image: busybox
    command:
    - cat
    tty: true
"""
) {
    node (label) {
      container('busybox') {
        sh "hostname"
      }
    }
}

```