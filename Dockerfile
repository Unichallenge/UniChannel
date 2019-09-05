FROM python

WORKDIR /app
COPY server/requirements.txt .

RUN pip install -r requirements.txt
RUN pip install uwsgi

COPY server .
COPY server/unichallenge/site_config.production.py unichallenge/site_config.py

CMD uwsgi --socket 0.0.0.0:8000 --protocol uwsgi --module unichallenge.wsgi