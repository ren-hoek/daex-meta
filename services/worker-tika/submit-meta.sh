#!/bin/bash
docker run  \
    --rm \
    --name submit \
    --hostname submit \
    --network docproc2 \
    --env S3_READ_BUCKET=coconut-zero \
    --env S3_WRITE_BUCKET=coconut-zero-writable \
    --env S3_READ_PATH=million/ \
    --env COLLECTION=million \
    --env PROFILE="" \
    --env SUBMIT=rqmeta \
    docker.service:5000/k8s-analysis/rq-tika submit.py

