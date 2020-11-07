FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/tracksideops
RUN mkdir /code/tracksideops/staticfiles
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./ /code/