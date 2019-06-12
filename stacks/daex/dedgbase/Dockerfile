FROM centos:latest
RUN yum -y update && \
    yum -y install yum-utils cmake && \
    yum -y groupinstall development && \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y epel-release unixODBC unixODBC-devel libxml2-devel libcurl-devel openssl-devel sssd-tools initscripts \
                   krb5-workstation krb5-libs krb5-auth-dialog enchant python-devel  udunits2-devel nlopt-devel cyrus-sasl-devel sudo \
                   wget zeromq-devel protobuf-devel v8-devel jq-devel ImageMagick-c++-devel mysql-devel gdal-python gdal-devel \
                   mapserver mapserver-python libxml2 libxml2-python python-lxml python-pip python-devel gcc gsl gsl-devel git ncurses-devel tmux
RUN yum -y install python36u python36u-pip python36u-devel && \
    rm /bin/pip && ln -s /bin/pip3.6 /bin/pip && \
    pip install --no-cache-dir -U pip && \
    pip install awscli --upgrade
RUN ln -s /usr/bin/python3.6 /usr/bin/python3
RUN git clone https://github.com/vim/vim && cd vim && \
    ./configure --prefix=/usr --with-features=huge --enable-multibyte --enable-cscope\
	--with-python3-config-dir=/usr/lib/python3.6/config --enable-python3interp=yes \
    make && make install
RUN mkdir ~/.vim && mkdir ~/.vim/bundle && \
  git clone https://github.com/Valloric/YouCompleteMe.git \
  ~/.vim/bundle/YouCompleteMe
WORKDIR /root/.vim/bundle/YouCompleteMe
RUN git submodule update --init --recursive && python3 install.py
WORKDIR /root
COPY .vimrc .
RUN git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
	vim +PluginInstall +qallvim +PluginInstall +qall  > /dev/null 2>&1

