FROM tiangolo/uwsgi-nginx:python3.5
RUN pip install -U pip falcon psycopg2
COPY uwsgi.ini /app/
RUN mkdir /code/
COPY *.py /code/
VOLUME /code/
