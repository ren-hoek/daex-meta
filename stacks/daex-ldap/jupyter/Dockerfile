FROM daex-meta/daexbase:ldap

RUN yum -y install nodejs && \
    npm install -g configurable-http-proxy
RUN pip install --no-cache-dir -U notebook jupyterhub jupyterlab jupyterhub-ldap-authenticator && \
    jupyter serverextension enable --py jupyterlab --sys-prefix

ADD init-ldap.sh /usr/bin/init-ldap.sh
RUN chmod +x /usr/bin/init-ldap.sh

ADD fork-ldap.sh /usr/bin/fork-ldap.sh
RUN chmod +x /usr/bin/fork-ldap.sh
ADD init-ldap.service /etc/systemd/system/init-ldap.service

ADD jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py
ADD jupyterhub.service /etc/systemd/system/jupyterhub.service
ADD init-jupyter.sh /usr/bin/init-jupyter.sh
RUN chmod +x /usr/bin/init-jupyter.sh

RUN systemctl enable jupyterhub.service
RUN systemctl enable init-ldap.service

CMD ["/usr/sbin/init"]

