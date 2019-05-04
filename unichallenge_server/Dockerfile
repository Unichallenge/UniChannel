FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /server
WORKDIR /server
COPY requirements.txt /server
RUN pip install -r requirements.txt
COPY . /server
RUN python manage.py collectstatic --noinput

CMD uwsgi --http :8000 --module unichallenge.wsgi
