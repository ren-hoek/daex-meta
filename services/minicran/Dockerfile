FROM docker.service:5000/daex-meta/dedgbase
RUN yum install -y R 
RUN R -e "install.packages(c('miniCRAN'), repos='https://cran.rstudio.com/')"
COPY minicran.R .
COPY pkgs.txt .
