FROM centos
RUN yum -y update
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u python36u-pip python36u-devel
RUN ln -s /bin/pip3.6 /bin/pip
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -U pip2pi
ADD requirements.txt .

