build:
	docker build -t docker.service:5000/daex-meta/jenkins:lts .

deploy:
	docker stack deploy -c docker-compose.yml jenkins

push:
	docker push docker.service:5000/daex-meta/jenkins:lts

stop:
	docker stack rm jenkins

clean:	
	docker image rm docker.service:5000/daex-meta/jenkins:lts
	docker image rm jenkins/jenkins:lts
	docker volume rm jenkins_home
