FROM docker.service:5000/daex-meta/daexbase
RUN yum install -y R 
RUN R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')"
