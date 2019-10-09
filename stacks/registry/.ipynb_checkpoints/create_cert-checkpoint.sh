openssl req \
  -newkey rsa:4096 -nodes -sha256 -keyout certs/docker.service.key \
  -x509 -days 365 -out certs/docker.service.crt \
  -subj "/C=GB/ST=Liverpool/L=Liverpool/O=daex/OU=devops/CN=daex.devops.com"
