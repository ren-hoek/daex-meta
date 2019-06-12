#!/bin/bash
docker build -t infra/pypi .
docker tag infra/pypi docker.service:5000/infra/pypi
