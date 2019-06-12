#!/bin/bash
#
# Build the worker docker image
#

IMAGE=k8s-analysis/rq-tika

# build the docker image
docker build -t "$IMAGE" .

docker tag $IMAGE docker.service:5000/$IMAGE
