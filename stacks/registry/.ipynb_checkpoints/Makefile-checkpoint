build:
	mkdir -p certs
	./create_cert.sh
	./secrets.sh
	docker pull registry:2
	docker pull centos

deploy:
	docker stack deploy -c docker-compose.yml registry
	./populate.sh
	docker service update --force registry_registry

stop:
	docker stack rm registry

clean:
	docker secret rm docker.service.crt 
	docker secret rm docker.service.key 
	rm -rf certs
	docker image rm registry:2
	docker image rm centos:latest 
	docker volume rm registry_certs
	docker volume rm registry_data
