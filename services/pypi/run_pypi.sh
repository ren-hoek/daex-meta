#!/bin/bash
docker run --rm --name pypi -v /data/nginx/html:/data/ -it docker.service:5000/infra/pypi bash
