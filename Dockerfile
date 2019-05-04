FROM node

RUN mkdir /angular
WORKDIR /angular
COPY unichallenge_client/package.json /angular
COPY unichallenge_client/package-lock.json /angular
RUN npm install
COPY unichallenge_client /angular
RUN npm run prod

FROM nginx

COPY --from=0 /angular/dist/uknow /files/angular
COPY unichallenge_server/static /files/static
