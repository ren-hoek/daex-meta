build:
	docker build -t docker.service:5000/daex-meta/nginx .

deploy-initial:
	docker stack deploy -c docker-compose.yml nginx
	./populate-initial.sh

deploy:
	docker stack deploy -c docker-compose.yml nginx
	./populate.sh

clean:
	docker stack rm nginx
