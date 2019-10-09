FROM docker.service:5000/daex-meta/daexbase
RUN yum -y install nodejs && \
    npm install -g configurable-http-proxy
RUN pip install --no-cache-dir -U notebook jupyterhub jupyterlab virtualenv && \
    jupyter serverextension enable --py jupyterlab --sys-prefix && \
    pip install --no-cache-dir -U spacy && \
    python3.6 -m spacy download en_core_web_md

ADD bin/start-jupyter.sh .
RUN chmod +x start-jupyter.sh
CMD ["./start-jupyter.sh"]

EXPOSE 8000
