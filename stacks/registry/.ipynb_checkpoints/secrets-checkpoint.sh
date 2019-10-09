#!/bin/bash
docker secret create docker.service.crt certs/docker.service.crt
docker secret create docker.service.key certs/docker.service.key
