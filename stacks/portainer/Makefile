build:
	docker pull portainer/portainer
	docker tag portainer/portainer docker.service:5000/portainer/portainer
	docker pull portainer/agent
	docker tag portainer/agent docker.service:5000/portainer/agent

deploy:
	docker stack deploy -c docker-compose.yml portainer

push:
	docker push docker.service:5000/portainer/agent
	docker push docker.service:5000/portainer/portainer

stop:
	docker stack rm portainer

clean:
	docker image rm docker.service:5000/portainer/portainer portainer/portainer
	docker image rm docker.service:5000/portainer/agent portainer/agent


