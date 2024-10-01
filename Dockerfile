FROM nginx
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install vim htop procps apt-transport-https build-essential net-tools iputils-ping
RUN apt-get -y install ca-certificates curl vim software-properties-common dnsutils tcpdump 
RUN apt-get -y install apache2-dev
RUN apt-get -y install apache2 apache2-utils libapache2-mod-wsgi-py3
RUN apt-get -y upgrade
RUN set -o vi
RUN mkdir -p /var/www/websites
COPY ./deploy-with-apache/websites /var/www/websites
RUN cp -r /etc/nginx/conf.d /etc/nginx/conf.d.bak
COPY ./deploy-with-apache/conf.d /etc/nginx/conf.d

COPY ./deploy-with-apache/apache-conf/ports.conf /etc/apache2/ports.conf
COPY ./deploy-with-apache/apache-conf/sites-enabled/000-default.conf /etc/apache2/sites-available/000-default.conf
RUN service apache2 start
EXPOSE 80/tcp
EXPOSE 8000
