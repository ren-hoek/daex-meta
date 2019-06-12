#!/bin/bash
docker service create \
	--name rqwork \
	--network docproc2 \
    	--env S3_READ_BUCKET=coconut-zero \
    	--env S3_WRITE_BUCKET=coconut-zero-writable \
    	--env S3_WRITE_PATH=testing/greenbookpdfs \
    	--env PROFILE="" \
	--replicas 2 \
	docker.service:5000/analysis/rq-regex worker.py
