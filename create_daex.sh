#!/bin/bash

# Install requests for pyport
pip3 install requests

# Set up swarm
docker swarm init
./network2.sh
./label_node.sh

# Create and deploy portainer
cd stacks/portainer
make build
make deploy
cd ../
bin/init_admin password localhost

# Set up Jenkins
# bin/build_image docker.service:5000/daex-meta/jenkins jenkins/ localhost
# bin/deploy_stack.py jenkins jenkins/docker-compose.yml localhost
# Additional command line setup
# bin/remove_stack jenkins localhost

# Create and deploy Gitlab
bin/build_image docker.service:5000/daex-meta/gitlab gitlab/ localhost
bin/deploy_stack gitlab gitlab/docker-compose.yml localhost

# Create and deploy RQ
bin/pull_image redis:latest localhost
bin/tag_image redis:latest docker.service:5000/redis:latest localhost
bin/build_image docker.service:5000/daex-meta/rqdash redis/ localhost
bin/deploy_stack redis redis/docker-compose.yml localhost

# Create and deploy MongoDB
bin/pull_image mongo:latest localhost
bin/tag_image mongo:latest docker.service:5000/mongo:latest localhost
bin/pull_image mongo-express:latest localhost
bin/tag_image mongo-express:latest docker.service:5000/mongo-express:latest localhost
bin/deploy_stack mongo mongo/docker-compose.yml localhost

# Create and deploy Daex
bin/build_image docker.service:5000/daex-meta/daexbase daex/daexbase/ localhost
bin/build_image docker.service:5000/daex-meta/rbase daex/rbase/ localhost
bin/build_image docker.service:5000/daex-meta/rstudio daex/rstudio/ localhost
bin/build_image docker.service:5000/daex-meta/shiny daex/shiny/ localhost
bin/build_image docker.service:5000/daex-meta/jupyterhub daex/jupyterhub/ localhost
bin/deploy_stack daex daex/docker-compose.yml localhost
bin/add_daex_user gavin localhost 

# Create and deploy Nginx
bin/build_image docker.service:5000/daex-meta/nginx nginx/ localhost
bin/deploy_stack nginx nginx/docker-compose.yml localhost
bin/add_folder nginx_nginx /etc/nginx nginx/nginx/ localhost
bin/add_folder nginx_nginx /usr/share/nginx/html nginx/html/ localhost
bin/redeploy_stack nginx nginx/docker-compose.yml localhost

