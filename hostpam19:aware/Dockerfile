# examen hostpam19
# isx4377298 curs 2019-20
# 28-11-19

FROM fedora:27
LABEL version="1.0"
LABEL author="@isx43577298 ASIX-M06"
LABEL subject="hostpam"
RUN dnf -y install vim procps util-linux-user finger passwd python 
RUN pip install python-pam
RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker
