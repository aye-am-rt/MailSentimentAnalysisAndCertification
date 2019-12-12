FROM python:3-alpine
#FROM alpine:latest

MAINTAINER Ritesh Tiwari

RUN apk add --update --no-cache --virtual .build-deps \
        g++ \
        python-dev \
        libxml2 \
        libxml2-dev && \
    apk add libxslt-dev && \
    apk del .build-deps

RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq

RUN apk update && \
    apk add bash && \
    apk add curl && \
    apk add vim && \
    apk add git && \
    apk add --no-cache python3-dev \
    && pip3 install --upgrade pip \
    && pip3 install Pillow==2.1.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .

EXPOSE 5000

#RUN cd src/main/python/com/cgi/AppCrt/controller/
#RUN ls
#RUN os.getcwd()

ENTRYPOINT ["python3"]

CMD ["src/main/python/com/cgi/AppCrt/services/__init__.py"]

#HEALTHCHECK --interval=5s --timeout=5s CMD curl --fail http://localhost:5000 || exit 1