# Dockerfile

Los experimentos con los diferentes tipos de Docker nos dejaron las siguientes conclusiones, los Docker creados con Python-alpine o python-slim-buster contienen el mínimo de espacio necesario para el correcto funcionamiento de nuestro sistema. 

La creación de un Docker con alpine, instalando python unicamente, nos dio una imagen muy ligera, que aunque no llegaba a tener tan poco peso como python-alpine era bastante aceptable. 

La imagen creada utilizando el sistema operativo fedora fue bastante ligera en comparación con las imágenes creadas utilizando pyhon-alpine y Python-slim-buster. 

Podemos observar los resultados obtenidos de la experimentación en la siguiente imagen:
![Pesos Dockers]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/example/Docker-pesos.jpg)

Procedí a diseñar un archivo Docker sencillo con alpine, debido a ser esta una de las opciones más populares y a que mi experimentación me llevo a concluir que esta era una de las imagenes más ligeras, adicionalmente me gusto tener la posibilidad de actualizar el software y establecer el entorno de python manualmente.

Explicaremos el contenido del Docker a continuación:

```
FROM alpine:3.10
MAINTAINER Oscar Rubio Garcia 

WORKDIR /code
ENV PORT="DEFAULT"

RUN apk update && apk upgrade && apk add py-pip linux-headers python3 py3-virtualenv bash 

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements-img.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm -rf requirements.txt

COPY LICENSE tasks.py setup.py /code/
COPY project /code/project

RUN addgroup -S dockergroup && adduser -S dockeruser -G dockergroup -h /code
USER dockeruser

CMD invoke runGunicornParams -p ${PORT}
```

Para empezar, establecemos la imagen utilizada a ser una imagen que contenga en este caso el sistema alpine, en nuestro caso decidimos usar la versión más actualizada de alpine, está siendo la versión 3.10. Después definimos el entorno de trabajo en la imagen Docker que crearemos, en este caso el entorno será el directorio /code, adicionalmente estableceremos el maintainer del Docker siendo yo como autor.

Tras esto, establecemos la variable de entorno PORT a ser igual a "DEFAULT". Esta variable de entorno será utilizada para poder definir el puerto en el que se desea lanzar el servicio. Le asignamos una variable "DEFAULT" debido a que nuestra herramienta de construcción invoke requiere aceptar al menos 1 parámetro existente, y de esta forma no revelamos el puerto por defecto que utilizara nuestro servicio.

Procedemos con la fase de preparación de la imagen Docker, aquí nos aseguramos de que el sistema esta actualizado y al día, tras actualizar el sistema procedemos a la instalación de aquellos programas indispensables para el correcto funcionamiento de nuestro microservicio. En nuestro caso instalaremos pip, las cabeceras de linux para prevenir errores, python3 con su entorno virtual y bash para poder dar uso de nuestra herramienta de construcción invoke.

Tras instalar python3 procedemos a asegurarnos que el entorno del entorno virtual de python es configurado correctamente con el fin de evitar posibles errores debidos a la falta de módulos. Este apartado fue desarrollado gracias al tutorial proporcionado en este [enlace.](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/) Básicamente lo que realizamos es el establecimiento de las variables de entorno de Python 3 en nuestra imagen Docker y asignando el correcto PATH, de esta forma permitiendo la ejecución de comandos Python desde los comandos CMD y RUN, si fuera necesario.

A continuación, empezamos el proceso de creación de la imagen Docker, copiamos el archivo de requirements-img.txt de nuestro proyecto, el cual contiene solamente las dependencias necesarias a instalar en la imagen Docker para que funcione el proyecto, a un archivo requirements.txt en la imagen Docker. Proseguimos utilizando pip para instalar todas las dependencias del archivo requirements.txt en la imagen Docker y después lo eliminamos. 

Después, copiamos el resto de los archivos del proyecto en el directorio /code que creamos anteriormente. Seleccionamos solo aquellos archivos que definimos como importantes para la imagen Docker.

Previamente a realizar la ejecución del servicio, crearemos un usuario nuevo en el docker, al que le asignaremos un grupo también recién creado y le asignaremos nuestro directorio actual de trabajo como directorio "home". De esta manera tendremos a un usuario corriente ejecutando el comando final de ejecución del servicio.

El paso final será la utilización del comando cmd para inicializar el microservicio, utilizamos nuestra herramienta de construcción invoke para invocar, en el caso del so Linux, Gunicorn como servidor de la aplicación para ejecutar el lanzamiento de nuestro api REST en la imagen del Docker. Damos uso del servidor de aplicaciones Gunicorn puesto que es un servidor estable y comúnmente utilizado en aplicaciones Python como la nuestra (por lo que contiene gran cantidad de documentación).

Para más información del comando de invoke vea el archivo [DefinicionTasks.md.](https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/DefinicionTasks.md )

Tras la creación del archivo Docker procedimos a su generación, despliegue y subida a Docker Hub utilizando los siguientes comandos:
* Docker image build . -t microservicionews:1.4

Usando este comando especificamos la creación de una imagen Docker basándonos en el directorio en el cual estamos situados y damos como tag a nuestro nombre el nombre de microservicionews con versión 1.3

Comprobamos la creación y tamaño de nuestra imagen Docker utilizando:

* Docker image ls

En nuestro caso el Docker fue creado con un tamaño de 138MB. 

Adicionalmente podríamos comprobar el numero de capas de nuestra imagen utilizando el siguiente comando:

* Docker history microservicionews:1.4

En nuestro caso comprobamos que tenernos 12 capas, 2 capas al principio que se combinan juntas debido a que forman parte del mismo comando, FROM alpine:3.10

Procedemos a probar el correcto comportamiento del docker:

* Docker container run --publish 5000:5000 --env PORT=5000 microservicionews:1.4

Este comando se encarga de ejecutar el Docker que especificamos como microservicionews:1.4 y de publicarlo al puerto 5000:5000 de nuestro ordenador, que es el puerto por predefinido que estamos utilizando con Python flask. De esta forma podrémos comprobar que el comportamiento es correcto utilizando la ip del docker-machine. Adicionalmente establece la variable de entorno PORT a ser 5000, para poder vincular ambos puertos.

* Docker login

Realizamos un login en el servidor de Docker hub, con el fin de tener los permisos necesarios para realizar la subida de la imagen al repositorio previamente creado.

* Docker tag microservicionews:1.4 oscarrubiogarcia/proyectoccdocker:microservicionews-v1.3-invoke

Cambiamos el tag de nuestra imagen para ser subida correctamente al repositorio de Docker Hub,

* Docker push oscarrubiogarcia/proyectoccdocker:microservicionews-v1.3-invoke

Comando utilizado para subir la imagen especificada como microservicionews al repositorio oscarrubiogarcia/proyectoccdocker. Destacaremos que previamente realizamos el comando Docker tag para cambiar el nombre de nuestro Docker.

Una vez realizados estos comandos obtendríamos la imagen del Docker creado de alpine, en nuestro repositorio de Docker hub. 

Finalmente comprobaré el rendimiento del docker utilizando la herramienta JMeter, pues esta es una herramienta muy sencilla de desplegar, instalar y aprender a utilizar. Con ella creamos el caso en el que 500 usuarios intentan acceder a nuestro servicio web, tanto a la pagina principal como a la pagina de las noticias, 3 veces. Los resultados son mostrados a continuación en forma de gráfico:

![Docker]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/JMeterGraph.jpg )

Podemos decir del grafico que nuestro despliegue actual podría soportar 500 usuarios en las condiciones descritas anteriormente fácilmente, esto lo deducimos de comparar la línea del “Throughput” con la de “Deviation”. En nuestro caso queremos siempre que el “Throughput” este lo más alto posible, mientras que “Deviation” este lo más bajo posible.

A continuación, desplegaremos el docker en heroku, para hacer esto tendremos que crear un archivo heroku.yml en nuestro proyecto, preferiblemente junto a nuestro archivo Dockerfile.

### Archivo heroku.yml

```python
build:
  docker:
    web: Dockerfile
```

Este archivo .yml solo deberá de identificar la imagen del Docker a crear en heroku, realizamos esto mediante los tags de build: - Docker: - web: indicando el Dockerfile que utilizara para la imagen. Debido a que nuestro Dockerfile ya contendrá los comandos de ejecución en su comando cmd, no estableceremos los tags run: para especificarlo en el archivo .yml.
Finalmente utilizaremos los comandos dados en la documentación oficial de heroku para realizar la subida del proyecto a un repositorio creado en heroku y finalmente su despliegue.
* Heroku git:remote -a newdashboardapi

Con este comando vincularemos el repositorio en el que nos encontramos con el repositorio en heroku newdashboardapi.

* Heroku stack:set container -a automatednewsapi

Con este comando estableceremos el stack del proyecto de heroku como de tipo container, para asegurarnos de que el contenedor sera creado. después especificamos la app a la que nos estamos refiriendo.

* Git push heroku master

Finalmente con este comando publicamos todos los cambios realizados en el repositorio en heroku y este desplegara automáticamente la imagen establecida en el dockerfile. También podremos realizar un despliegue manual desde heroku mediante el menu de Deploy.

Mostramos a continuación 2 pequeñas capturas demostrando la subida y despliegue con éxito tanto del Docker a Docker hub como del Docker a Heroku.

![Docker]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/DockerHub.jpg )
![Heroku]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Heroku-Docker.jpg )

## Automatización Docker Hub
Con el fin de automatizar la subida y despliegue del archivo Dockerfile creado, crearemos un repositorio nuevo automatizado en Docker Hub, vinculando previamente nuestra cuenta de GitHub con Docker Hub. Vincularemos nuestro proyecto GitHub CCProyecto para la automatización del build y subida a DockerHub, básicamente para no tener que utilizar todos los comandos previamente usados. Aquí podemos ver la confirmación de la automatización en Docker Hub.

![Imagen Docker Hub]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/DockerAutomated.jpg)

También se automatizo el despliegue en Heroku:

![Heroku Auto]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Heroku-Docker-Automated.jpg )

## Fuentes
Se utilizo el tutorial mostrado en [este enlace](https://runnable.com/docker/python/dockerize-your-flask-application) para la recaudación de información relacionada con la construcción del Docker. 

Adicionalmente también fue utilizada la documentación proporcionada por dockerhub y heroku para el correcto despliegue y automatización del Docker. 
* [Documentación heroku](https://blog.heroku.com/build-docker-images-heroku-yml)
* [Documentación docker hub](https://docs.docker.com/docker-hub/)
* [Documentación docker hub automatización](https://docs.docker.com/docker-hub/builds/)