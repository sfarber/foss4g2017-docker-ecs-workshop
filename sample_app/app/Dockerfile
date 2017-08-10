FROM tiangolo/uwsgi-nginx:python3.5
RUN pip install -U pip falcon psycopg2
COPY uwsgi.ini /app/
VOLUME /code/
EXPOSE 80
