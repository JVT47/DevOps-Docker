#/bin/bash

GIT_REPO=$1
DOCKER_REPO=$2
DOCKER_USER=${3}
DOCKER_PWD=${4} 

git clone https://github.com/$GIT_REPO cloned-repo

cd cloned-repo


echo $DOCKER_PWD | docker login --username $DOCKER_USER --password-stdin

docker build . -t $DOCKER_REPO

docker push $DOCKER_REPO
