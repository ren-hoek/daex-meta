FROM docker.service:5000/daex-meta/daexbase
RUN yum -y install nodejs && \
    npm install -g configurable-http-proxy
RUN pip install --no-cache-dir -U notebook jupyterhub jupyterlab && \
    jupyter serverextension enable --py jupyterlab --sys-prefix
ADD bin/start-jupyter.sh .
RUN chmod +x start-jupyter.sh
CMD ["./start-jupyter.sh"]

EXPOSE 8000
