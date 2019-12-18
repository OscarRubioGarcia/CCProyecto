# Cambios previos a la experimentación

Con el objetivo de poder desplegar correctamente el microservicio de noticias fue necesario realizar ciertos cambios tanto al Dockerfile como al código del sistema con el fin de que este pudiera dar uso de nuestra base de datos Cassandra. 

## Cambios en el Dockerfile
Se añadieron los programas necesarios para la realización del despliegue de cassandra y se tubo que eliminar la generación de un usuario normal, debido a problemas con el despliegue de Cassandra.

```
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
```

Estos cambios espero que sean temporales, pues espero poder lanzar todo el sistema utilizando un usuario normal y no root.

## Cambios en el código

Previamente a la comprobación del servicio prestado con Taurus, se incorporo un sistema de cache en el microservicio, proporcionado por Flask-Caching. Utilizando este servicio esperamos conseguir una mejora a la hora de servir servicios similares a los clientes.

# Experimentación con Taurus

Nuestro objetivo principal con esta experimentación será de conseguir que nuestro sistema pueda soportar un mínimo de 1000 peticiones de 10 usuarios durante varios segundos.

Utilizaremos la herramienta Taurus obtenible [aquí ]( https://gettaurus.org/ ) para realizar la creación de estos Benchmarks.


