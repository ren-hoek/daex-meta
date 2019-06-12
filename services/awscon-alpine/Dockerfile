FROM alpine

COPY copyfiles .

RUN apk update && apk add --no-cache cmake g++ make python3-dev less groff curl \
	sudo tmux vim git wget curl tini bash openssh-client && \
	pip3 install --no-cache-dir --upgrade pip && \
	pip3 install --no-cache-dir --upgrade awscli boto3 pymongo redis rq elasticsearch && \
	addgroup -S aws && \
	adduser -D -S -s /bin/bash -G aws aws && \
	mv sudo-users /etc/sudoers.d && \ 
	tar xvzf aws.tar.gz && mv aws .aws && \
	tar xvzf ssh.tar.gz && mv ssh .ssh && \
	tar xvzf vim.tar.gz && \
	rm aws.tar.gz ssh.tar.gz vim.tar.gz && \
	mv /.bashrc /home/aws && mv /.bash_profile /home/aws && \
	mv /.gitconfig /home/aws && mv /.tmux.conf /home/aws && \
	mv /.vimrc /home/aws 

WORKDIR /vim/bundle/YouCompleteMe

RUN python3 install.py && \
	mv /vim /home/aws/.vim && \
	chown -R aws:aws /home/aws

USER aws
WORKDIR /home/aws

