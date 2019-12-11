FROM python:3-alpine

MAINTAINER Ritesh Tiwari

COPY src/main/ /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 8080
#
#CMD [ "python", "./run.py" ]