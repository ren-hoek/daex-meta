#!/bin/bash
cd conf-initial
docker run -v nginx_conf:/data --name helper centos true 
docker cp . helper:/data
docker rm helper
docker service update --force nginx_nginx
