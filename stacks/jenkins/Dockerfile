FROM jenkins/jenkins:lts-alpine
USER root
RUN apk add --no-cache --update python3 && \
     pip3 install -U pip && \
     pip3 install -i https://test.pypi.org/simple/ pyport

USER jenkins

# install jenkins plugins
RUN /usr/local/bin/install-plugins.sh git workflow-aggregator

# allows to skip Jenkins setup wizard
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

# Jenkins runs all grovy files from init.groovy.d dir
# use this for creating default admin user
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/
