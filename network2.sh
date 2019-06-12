#!/bin/bash
docker network create \
	--driver overlay \
	-o "com.docker.network.bridge.enable_ip_masquerade"="true" \
	--attachable docproc2
