[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/OscarRubioGarcia/CCProyecto.svg?branch=master)](https://travis-ci.org/OscarRubioGarcia/CCProyecto)
[![codecov](https://codecov.io/gh/OscarRubioGarcia/CCProyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/OscarRubioGarcia/CCProyecto)

## Titulo del proyecto

Campus Dashboard

## Descripción del proyecto

Definiremos nuestro sistema dirigido al ámbito escolar, específicamente a la formación de grupos sociales entre estudiantes de un establecimiento escolar y a la notificación de nuevas noticias.

La aplicación en si será parecida a un tablón de anuncios, una aplicación dedicada a ayudar en la creación de grupos de estudiantes (clubs) y mantenerles informados de noticias ocurriendo en su campus. Adicionalmente los estudiantes podrán realizar comentarios acerca de clubs y noticias.

De esta forma el usuario podrá buscar clubs en la base de datos y decidir si desea unirse a estos, buscar las noticias que estén ocurriendo en el campus, ver los comentarios de algún club/noticia o realizar comentarios acerca de un club o noticia. Adicionalmente tendremos un bot en Telegram el cual será utilizado por los estudiantes para comunicarse con el sistema.

Esta aplicación contendrá inicialmente las siguientes facultades:
* Gestión de clubs. 
* Gestión de noticias.
* Gestión de comentarios
* Bot de Telegram para inicializar los servicios.

### Microservicios planteados

 * Gestión de Noticias
 * Gestión de Clubs
 * Gestión de Comentarios

## La Arquitectura de los Microservicios

Para conocer en más detalle la arquitectura del sistema, siguan este 
[enlace al documento.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/Arquitectura.md )

## Herramienta de Construcción

Daremos uso de Invoke como nuestra herramienta de construcción para nuestro proyecto en Python. Esta esta localizada en tasks.py.

[Descripción del fichero tasks.py.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/DefinicionTasks.md )

## Framework de Testing Local

Con el fin de mantener la integración de nuevos módulos o cambios en nuestro proyecto, libre de fallos, utilizare el framework unitTest. Con este framework podré definir los pasos necesarios para el correcto testing de cada uno de mis microservicios, asegurándome que durante los “tests” se realizan los procesos de setUp, testing y tearDown correctamente. De esta forma estableceré un sistema de testing local que me permitirá comprobar si mis microservicios siguen siendo funcionales a medida que los incorporo o modifico.

Para más informacion de los tests siguan el 
[enlace a la descripción de los tests.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/Tests.md )

## Integración Continua en la Nube

Daremos uso de TravisCI para la integración continua del proyecto en el repositorio. Travis se encargará de instalar todas las dependencias y lenguajes de programación que fueran necesarios en nuestro proyecto y realizara los tests desarrollados con unitTest por nosotros. Utilizando TravisCI conseguiremos comprobar el funcionamiento correcto de nuestros tests en diversas versiones de Python y monitorizar los posibles errores que puedan ocurrir. TravisCI al estar montado en la nube será perfecto para nosotros a la hora de comprobar la integración continua de nuestro proyecto también en la nube.

Para más informacion del archivo .travis.yml siguan el 
[enlace a la descripción del fichero .travis.yml.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/Travis.md )

## Docker del proyecto

Realicé diversos experimentos utilizando los contenedores Docker y varios sistemas operativos con la finalidad de conseguir un Docker con el mínimo tamaño, estos experimentos pueden verse en el siguiente [directorio.]( https://github.com/OscarRubioGarcia/CC/tree/master/example) La experimentación de estos archivos Docker puede ser encontrada al final de este apartado.

Procedí a diseñar un archivo Docker sencillo con alpine, debido a ser esta una de las opciones más populares y a que mi experimentación me llevo a concluir que esta era una de las imagenes más ligeras, adicionalmente me gusto tener la posibilidad de actualizar el software y establecer el entorno de python manualmente.

**Contenido del fichero Dockerfile:**

```
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

CMD [ "invoke", "runGunicornParams", "-p", "5000" ]
```

Adicionalmente realicé la subida del Docker tanto a Docker hub como a un repositorio creado en Heroku, a través del cual podemos comprobar el correcto comportamiento de la imagen Docker.

Contenedor: https://hub.docker.com/r/oscarrubiogarcia/proyectoccdocker

La imagen actual del sistema está bajo el tag: microservicionews-v1.3-invoke-gunicorn

El Docker utilizado para la subida a Heroku usaba el siguiente comando CMD en vez del mostrado anteriormente:

```
CMD [ "invoke", "runGunicorn", "-p", "5000" ]
```

Esto se debe a que heroku dinámicamente  asigna los puertos de nuestra app, por lo que no podemos establecer puertos fijos. 

Contenedor en Heroku: https://newdashboardapi.herokuapp.com/news

Para más información con relación a la experimentación realizada y la creación de la imagen Docker, tanto el archivo dockerfile creado o el archivo heroku.yml, pueden seguir [el enlace a la descripción del dockerfile.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/Docker.md )

## Despliegue del proyecto

Téngase en cuenta que este proyecto fue diseñado utilizando el software PyCharm para su creación y su testing local.

Para el correcto funcionamiento del proyecto se deberá tener en cuenta todas las librerías especificadas en "requirements.txt" y se deberá tener una versión valida de Python instalada en el sistema (Para más información de las versiones de Python validas, véase el archivo de pruebas “.travis.yml”).

## Historias de Usuario

Para obtener más información acerca de las historias de usuario desarrolladas para este proyecto visite el siguiente enlace: 
[Historias de Usuario]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/UserStories.md )

## Licencia

El proyecto será generado con una licencia de tipo GNU. Esta licencia no impone muchas limitaciones sobre la reutilización. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.
