FROM daex-meta/rbase:ldap

RUN R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')"
RUN wget https://download3.rstudio.org/centos6.3/x86_64/shiny-server-1.5.9.923-x86_64.rpm && \
    yum install --nogpgcheck -y shiny-server-1.5.9.923-x86_64.rpm

#COPY install-packages.r /tmp/R/
#RUN R -f /tmp/R/install-packages.r


ADD bin/shiny-server.sh .
RUN chmod +x shiny-server.sh
CMD ["./shiny-server.sh"]

EXPOSE 3838
