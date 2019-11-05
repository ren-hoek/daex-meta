#!/bin/bash

# Install requests for pyport
pip3 install -i https://test.pypi.org/simple/ pyport

# Set up swarm
docker swarm init
./network2.sh
./label_node.sh

# Set up build tools

# Create and deploy portainer
cd stacks/portainer
make build
make deploy
cd ../
init_admin password localhost

# Create and deploy registry
docker pull registry:2 localhost
deploy_stack registry registry/docker-compose.yml localhost

# Create and deploy Gitlab
cd gitlab
docker build -t docker.service:5000/daex-meta/gitlab .
deploy_stack gitlab gitlab/docker-compose.yml localhost
cd ..

# Set up Jenkins
cd jenkins
docker build -t docker.service:5000/daex-meta/jenkins .
deploy_stack jenkins jenkins/docker-compose.yml localhost

# Create and deploy Nginx
build_image docker.service:5000/daex-meta/nginx nginx/ localhost
deploy_stack nginx nginx/docker-compose.yml localhost
add_folder nginx_nginx /etc/nginx nginx/nginx/ localhost
add_folder nginx_nginx /usr/share/nginx/html nginx/html/ localhost
redeploy_stack nginx nginx/docker-compose.yml localhost

