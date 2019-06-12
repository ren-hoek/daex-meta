FROM docker.service:5000/daex-meta/rbase

RUN wget https://download2.rstudio.org/server/centos6/x86_64/rstudio-server-rhel-1.2.1335-x86_64.rpm && \
    yum install -y rstudio-server-rhel-1.2.1335-x86_64.rpm && \
    echo "server-app-armor-enabled=0" >> /etc/rstudio/rserver.conf

ADD bin/start-rserver.sh .
RUN chmod +x start-rserver.sh
CMD ["./start-rserver.sh"]

EXPOSE 8787
