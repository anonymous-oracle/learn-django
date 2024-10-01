FROM nginx
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install vim htop procps apt-transport-https build-essential net-tools iputils-ping
RUN apt-get -y install ca-certificates curl vim software-properties-common dnsutils tcpdump 
RUN apt-get -y upgrade
RUN set -o vi
RUN cp -r /etc/nginx/conf.d /etc/nginx/conf.d.bak
COPY ./deploy-with-apache/conf.d /etc/nginx/conf.d

EXPOSE 80/tcp


ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]
