FROM node

RUN mkdir /angular
WORKDIR /angular
COPY unichallenge_client /angular
RUN npm i && npm run prod

FROM nginx

COPY --from=0 /angular/dist/uknow /static
COPY unichallenge_server/static /static/static
