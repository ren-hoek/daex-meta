#!/bin/bash
mkdir -p /etc/docker/certs.d/docker.service:5000/
cp certs/domain.crt /etc/docker/certs.d/docker.service:5000/ca.crt
