FROM python:3.7-alpine
MAINTAINER Aniket Singla

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk upgrade --update && apk add --no-cache jpeg-dev zlib-dev  &&\
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
# RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user