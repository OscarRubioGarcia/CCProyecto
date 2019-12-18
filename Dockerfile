FROM alpine:3.10

MAINTAINER Oscar Rubio Garcia 

WORKDIR /code
ENV PORT="DEFAULT"

RUN apk update && apk upgrade && apk add py-pip linux-headers python3 py3-virtualenv python-dev bash openjdk8-jre wget

RUN wget http://archive.apache.org/dist/cassandra/3.11.4/apache-cassandra-3.11.4-bin.tar.gz \
    && tar -xzvf apache-cassandra-3.11.4-bin.tar.gz \
    && rm -rf apache-cassandra-3.11.4-bin.tar.gz

RUN mkdir /var/lib/cassandra /var/log/cassandra

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements-img.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm -rf requirements.txt

COPY LICENSE tasks.py setup.py /code/
COPY project /code/project

CMD invoke runGunicornCassandraParams -p ${PORT}
