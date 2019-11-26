FROM alpine:3.10
MAINTAINER Oscar Rubio Garcia 

WORKDIR /code

RUN apk update && apk upgrade 
RUN apk add --update py-pip
RUN apk add linux-headers python3 py3-virtualenv bash

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements-img.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD [ "invoke", "runPython" ]
