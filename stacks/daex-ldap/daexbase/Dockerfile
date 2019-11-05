FROM centos/system

RUN yum -y update && \
    yum -y install yum-utils cmake && \
    yum -y groupinstall development && \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm ncurses-devel \ 
           libcurl-devel sudo git tmux wget openldap-clients nss-pam-ldapd authconfig 

RUN yum -y install python36u python36u-pip python36u-devel && \
    pip3 install --no-cache-dir -U pip
RUN pip3 install awscli --upgrade
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
