#!/bin/bash
docker service create \
	--name rqtika \
	--network docproc2 \
    	--env S3_READ_BUCKET=coconut-zero \
    	--env S3_WRITE_BUCKET=coconut-zero-writable \
    	--env S3_READ_PATH=million/ \
    	--env COLLECTION=million \
    	--env PROFILE="" \
    	--env SUBMIT=rqmeta \
	--replicas 2 \
    	docker.service:5000/k8s-analysis/rq-meta worker.py
