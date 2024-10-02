FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install vim htop procps apt-transport-https build-essential net-tools iputils-ping
RUN apt-get -y install ca-certificates curl vim software-properties-common dnsutils tcpdump 
RUN apt-get -y install apache2-dev
RUN apt-get -y install apache2 apache2-utils libapache2-mod-wsgi-py3
RUN apt-get -y install python3-full python3-pip lsof
RUN apt-get -y upgrade
RUN set -o vi

COPY . /blog-app
WORKDIR /blog-app
RUN pip install -r requirements.txt --break-system-packages
WORKDIR /
EXPOSE 80

COPY ./deploy-with-apache/apache-conf/ports.conf /etc/apache2/ports.conf
COPY ./deploy-with-apache/apache-conf/sites-enabled/000-default.conf /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod proxy_http
RUN a2ensite 000-default.conf
RUN service apache2 restart
COPY ./startup.sh /startup.sh
RUN chmod +x /startup.sh
ENTRYPOINT [ "./startup.sh" ]