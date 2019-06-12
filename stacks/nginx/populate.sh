#!/bin/bash
docker run -v nginx_html:/data --name helper centos true 
cd html
docker cp . helper:/data
docker rm helper
cd ../conf
docker run -v nginx_conf:/data --name helper centos true
docker cp . helper:/data
docker rm helper
docker service update --force nginx_nginx
