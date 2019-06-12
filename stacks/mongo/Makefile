build:
	docker pull mongo
	docker tag mongo docker.service:5000/mongo
	docker pull mongo-express
	docker tag mongo-express docker.service:5000/mongo-express

push:
	docker push docker.service:5000/mongo
	docker push docker.service:5000/mongo-express

deploy:
	docker stack deploy -c docker-compose.yml mongo

stop:
	docker stack rm mongo

clean:
	docker image rm docker.service:5000/mongo mongo
	docker image rm docker.service:5000/mongo-express mongo-express

