FROM alpine:3.10
MAINTAINER Oscar Rubio Garcia 

WORKDIR /code

RUN apk update && apk upgrade && apk add py-pip linux-headers python3 py3-virtualenv bash 

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements-img.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD [ "invoke", "runGunicorn" ]
