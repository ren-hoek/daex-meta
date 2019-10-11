#!/bash

# Set up swarm
docker swarm init
./network2.sh
./label_node.sh

# Create and deploy portainer
cd stacks/portainer
make build
make deploy

# executor container

cd ../
bin/init_admin password localhost

# Install requests for pyport
pip3 install -i https://test.pypi.org/simple/ pyport
cd /home/gavin/Projects/daex-meta/stacks

# Set up Jenkins
build_image docker.service:5000/daex-meta/jenkins jenkins/
deploy_stack jenkins jenkins/docker-compose.yml

# Create and deploy secure registry
# cd registry
# mkdir -p certs
# ./create_cert.sh
# add_secret docker.service.crt certs/docker.service.crt
# add_secret docker.service.key certs/docker.service.key
# cd ..
# pull_image registry:2
# deploy_stack registry registry/docker-compose.yml.secure
# add_folder registry_registry /certs registry/certs/
# redeploy_stack registry registry/docker-compose.yml.secure

# Create and deploy registry
pull_image registry:2
deploy_stack registry registry/docker-compose.yml

# Create and deploy Gitlab
build_image docker.service:5000/daex-meta/gitlab gitlab/
deploy_stack gitlab gitlab/docker-compose.yml

# Jenkins build

# Create and deploy RQ
pull_image redis:latest
tag_image redis docker.service:5000/redis
build_image docker.service:5000/daex-meta/rqdash redis/
deploy_stack redis redis/docker-compose.yml

# Create and deploy MongoDB
pull_image mongo:latest
tag_image mongo docker.service:5000/mongo
pull_image mongo-express:latest
tag_image mongo-express docker.service:5000/mongo-express
deploy_stack mongo mongo/docker-compose.yml

# Create and deploy Daex
build_image docker.service:5000/daex-meta/daexbase daex/daexbase/
build_image docker.service:5000/daex-meta/rbase daex/rbase/
build_image docker.service:5000/daex-meta/rstudio daex/rstudio/
build_image docker.service:5000/daex-meta/shiny daex/shiny/
build_image docker.service:5000/daex-meta/jupyterhub daex/jupyterhub/
deploy_stack daex daex/docker-compose.yml
add_daex_user gavin 

# Create and deploy Nginx
build_image docker.service:5000/daex-meta/nginx nginx/
deploy_stack nginx nginx/docker-compose.yml
add_folder nginx_nginx /etc/nginx nginx/nginx/
add_folder nginx_nginx /usr/share/nginx/html nginx/html/
redeploy_stack nginx nginx/docker-compose.yml

