#!/bash

# Install requests for pyport
pip3 install -i https://test.pypi.org/simple/ pyport
cd /home/gavin/Projects/daex-meta/stacks

# Set up Jenkins
# build_image docker.service:5000/daex-meta/jenkins jenkins/
# deploy_stack.py jenkins jenkins/docker-compose.yml
# Additional command line setup
# remove_stack jenkins localhost

# Create and deploy Registry
cd registry
mkdir -p certs
./create_cert.sh
docker secret create docker.service.crt certs/docker.service.crt

# Create and deploy Gitlab
build_image docker.service:5000/daex-meta/gitlab gitlab/
deploy_stack gitlab gitlab/docker-compose.yml

# Create and deploy RQ
pull_image redis:latest
tag_image redis:latest docker.service:5000/redis:latest
build_image docker.service:5000/daex-meta/rqdash redis/
deploy_stack redis redis/docker-compose.yml

# Create and deploy MongoDB
pull_image mongo:latest
tag_image mongo:latest docker.service:5000/mongo:latest
pull_image mongo-express:latest
tag_image mongo-express:latest docker.service:5000/mongo-express:latest
deploy_stack mongo mongo/docker-compose.yml

# Create and deploy Daex
build_image docker.service:5000/daex-meta/daexbase daex/daexbase/ localhost
build_image docker.service:5000/daex-meta/rbase daex/rbase/ localhost
build_image docker.service:5000/daex-meta/rstudio daex/rstudio/ localhost
build_image docker.service:5000/daex-meta/shiny daex/shiny/ localhost
build_image docker.service:5000/daex-meta/jupyterhub daex/jupyterhub/ localhost
deploy_stack daex daex/docker-compose.yml localhost
add_daex_user gavin localhost 

# Create and deploy Nginx
build_image docker.service:5000/daex-meta/nginx nginx/ localhost
deploy_stack nginx nginx/docker-compose.yml localhost
add_folder nginx_nginx /etc/nginx nginx/nginx/ localhost
add_folder nginx_nginx /usr/share/nginx/html nginx/html/ localhost
redeploy_stack nginx nginx/docker-compose.yml localhost

