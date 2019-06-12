build:
	docker build -t docker.service:5000/daex-meta/gitlab .

deploy:
	docker stack deploy -c docker-compose.yml gitlab

push:
	docker push docker.service:5000/daex-meta/gitlab

stop:
	docker stack rm gitlab

clean:
	docker image rm docker.service:5000/daex-meta/gitlab
	docker image rm gitlab/gitlab-ce
	docker volume rm gitlab_config
	docker volume rm gitlab_logs
	docker volume rm gitlab_data




