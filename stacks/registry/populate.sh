#!/bin/bash
docker run -v registry_certs:/data --name helper centos true 
cd certs
docker cp . helper:/data
docker rm helper
