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
pull_image registry:2 localhost
deploy_stack registry registry/docker-compose.yml localhost

# Create and deploy Gitlab
build_image docker.service:5000/daex-meta/gitlab gitlab/ localhost
deploy_stack gitlab gitlab/docker-compose.yml localhost

# Set up Jenkins
build_image docker.service:5000/daex-meta/jenkins jenkins/ localhost
deploy_stack jenkins jenkins/docker-compose.yml localhost

# Create and deploy Nginx
build_image docker.service:5000/daex-meta/nginx nginx/ localhost
deploy_stack nginx nginx/docker-compose.yml localhost
add_folder nginx_nginx /etc/nginx nginx/nginx/ localhost
add_folder nginx_nginx /usr/share/nginx/html nginx/html/ localhost
redeploy_stack nginx nginx/docker-compose.yml localhost

# Deploy services

# Create and deploy RQ
pull_image redis:latest localhost
tag_image redis:latest docker.service:5000/redis:latest localhost
build_image docker.service:5000/daex-meta/rqdash redis/ localhost
deploy_stack redis redis/docker-compose.yml localhost

# Create and deploy MongoDB
pull_image mongo:latest localhost
tag_image mongo:latest docker.service:5000/mongo:latest localhost
pull_image mongo-express:latest localhost
tag_image mongo-express:latest docker.service:5000/mongo-express:latest localhost
deploy_stack mongo mongo/docker-compose.yml localhost

# Create and deploy Daex
build_image docker.service:5000/daex-meta/daexbase daex/daexbase/ localhost
build_image docker.service:5000/daex-meta/rbase daex/rbase/ localhost
build_image docker.service:5000/daex-meta/rstudio daex/rstudio/ localhost
build_image docker.service:5000/daex-meta/shiny daex/shiny/ localhost
build_image docker.service:5000/daex-meta/jupyterhub daex/jupyterhub/ localhost
deploy_stack daex daex/docker-compose.yml localhost
add_daex_user gavin localhost 

