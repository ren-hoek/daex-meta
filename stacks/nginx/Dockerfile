FROM nginx
RUN apt-get -y update && apt-get -y install openssl python3-pip && pip3 install --no-cache -U pip
RUN pip3 install awscli
RUN usermod -aG shadow nginx
COPY bin/certs.sh .
COPY bin/start-nginx.sh .
CMD ["./start-nginx.sh"]
