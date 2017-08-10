FROM postgres:latest
RUN apt-get update
RUN apt-get -y install postgis

COPY *.sql /docker-entrypoint-initdb.d/
COPY *.sh /docker-entrypoint-initdb.d/
