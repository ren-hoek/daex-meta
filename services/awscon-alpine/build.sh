#!/bin/bash
#
# Build the  docker image
#


cp -r $HOME/.aws aws
cp -r $HOME/.ssh ssh
cp -r $HOME/.vim vim


# tar the python code
tar -czvf copyfiles/aws.tar.gz aws
tar -czvf copyfiles/vim.tar.gz vim
tar -czvf copyfiles/ssh.tar.gz ssh

# build the docker image
docker-compose build

rm -rf aws
rm -rf ssh
rm -rf vim

rm copyfiles/aws.tar.gz
rm copyfiles/vim.tar.gz
rm copyfiles/ssh.tar.gz

