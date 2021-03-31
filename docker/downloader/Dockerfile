FROM ubuntu:latest

MAINTAINER "UltraDesu <ultardesu@hexor.ru>"

RUN apt update
RUN apt install -y wget ca-certificates mysql-client aria2
COPY backup_downloader.sh /
ENTRYPOINT bash backup_downloader.sh