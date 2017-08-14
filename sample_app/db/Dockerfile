FROM postgres:latest
RUN apt-get update
RUN apt-get -y install postgis

COPY *.sql /docker-entrypoint-initdb.d/
COPY 1_init_postgis.sh /docker-entrypoint-initdb.d/
