FROM node

RUN mkdir /angular
WORKDIR /angular
COPY unichallenge_client /angular
RUN npm i && npm run prod

FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /server
WORKDIR /server
COPY unichallenge/requirements.txt /server
RUN pip install -r requirements.txt
COPY unichallenge /server
COPY --from=0 /angular/dist/uknow /server/unichallenge/static
RUN python manage.py collectstatic
