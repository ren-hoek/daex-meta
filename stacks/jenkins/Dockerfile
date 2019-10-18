FROM jenkins/jenkins:lts-alpine
USER root
RUN apk add --no-cache --update python3 docker && \
     pip3 install -U pip
RUN  pip3 install -U -i https://test.pypi.org/simple/ pyport
RUN addgroup jenkins ping

USER jenkins

# install jenkins plugins
RUN /usr/local/bin/install-plugins.sh git workflow-aggregator docker-workflow

# allows to skip Jenkins setup wizard
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

# Jenkins runs all grovy files from init.groovy.d dir
# use this for creating default admin user
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/
