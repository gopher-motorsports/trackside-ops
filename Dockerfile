FROM python:3.6.7-alpine
RUN apk update \
    && apk add --virtual build-deps gcc musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/staticfiles
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apk del build-deps
ADD ./ /code/