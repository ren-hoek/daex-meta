FROM nginx
RUN apt-get -y update
RUN apt-get -y install openssl python3-pip && \
	pip3 install -U pip
RUN pip3 install awscli
RUN usermod -aG shadow nginx
COPY bin/certs.sh .
COPY bin/start-nginx.sh .
CMD ["./start-nginx.sh"]
