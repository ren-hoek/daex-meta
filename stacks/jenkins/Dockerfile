FROM jenkins/jenkins:lts
USER root
RUN apt-get update && \
    apt-get -y install apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
     "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
     $(lsb_release -cs) \
     stable" && \
    apt-get update && \
    apt-get -y install docker-ce && \
    usermod -aG docker jenkins
RUN apt-get -y install python3-pip && \
     pip3 install -U pip && \
     pip3.5 install -i https://test.pypi.org/simple/ pyport
USER jenkins
