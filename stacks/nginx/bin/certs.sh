#!/bin/bash
openssl req -x509 -nodes -days 365 \
	-newkey rsa:2048 \
	-subj "/C=UK/ST=State/L=City/O=Org/CN=daex" \
	-keyout /etc/nginx/nginx.key \
	-out /etc/nginx/nginx.crt
