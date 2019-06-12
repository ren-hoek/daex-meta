build:
	docker pull redis
	docker tag redis docker.service:5000/redis
	docker build -t docker.service:5000/daex-meta/rqdash .

push:
	docker push docker.service:5000/redis
	docker push docker.service:5000/daex-meta/rqdash

deploy:
	docker stack deploy -c docker-compose.yml redis

stop:
	docker stack rm redis

clean:
	docker image rm docker.service:5000/redis redis
	docker image rm docker.service:5000/daex-meta/rqdash

