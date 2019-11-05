FROM daex-meta/rbase:ldap

RUN wget https://download2.rstudio.org/server/centos6/x86_64/rstudio-server-rhel-1.2.1335-x86_64.rpm && \
    yum install -y rstudio-server-rhel-1.2.1335-x86_64.rpm && \
    echo "server-app-armor-enabled=0" >> /etc/rstudio/rserver.conf

COPY cacerts.pem /etc/openldap/certs/cert.pem
ADD init-ldap.sh /usr/bin/init-ldap.sh
RUN chmod +x /usr/bin/init-ldap.sh
ADD fork-ldap.sh /usr/bin/fork-ldap.sh
RUN chmod +x /usr/bin/fork-ldap.sh

ADD rstudio /etc/pam.d/rstudio
ADD rstudio-server.service /etc/systemd/system/rstudio-server.service
RUN systemctl enable rstudio-server.service
ADD init-ldap.service /etc/systemd/system/init-ldap.service
RUN systemctl enable init-ldap.service

CMD ["/usr/sbin/init"]

