FROM node

WORKDIR /angular
COPY unichallenge_client /code/
RUN npm i && npm run prod

FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY unichallenge /code/
COPY --from=0 /code/dist /code/static/
