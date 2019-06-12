#!/bin/bash
docker run  \
    --rm \
    --network docproc \
    --name submit \
    --hostname submit \
    --env S3_READ=palmwine2
    --env S3_WRITE=palmwine2-writable
    --env PROFILE=""
    --env SUBMIT=rqregex
    docker.service:5000/analysis/rq-regex submit.py

