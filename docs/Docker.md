# Dockerfile

Inicialmente diseñe un archivo Docker sencillo con alpine, debido a ser esta una de las opciones mas populares y a ser bastante ligera. Este archivo Docker inicial tenia la siguiente apariencia, la cual iremos explicando a continuación:

```python
FROM python:3.7-alpine
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD ["python", "project/Main.py"]
```

Para empezar, establecemos la imagen utilizada a ser una imagen que contenga Python y en este caso el sistema alpine, específicamente la versión 3.7 de python pues esta es la que utilizamos para la creación del proyecto. Después definimos el entorno de trabajo en la imagen Docker que crearemos, en este caso el entorno será el directorio /code. 

A continuación, empezamos el proceso de creación de la imagen Docker, copiamos el archivo de requirements.txt de nuestro proyecto, el cual contiene las dependencias a instalar para que funcione el proyecto, a un archivo requirements.txt en la imagen Docker. Proseguimos utilizando pip para instalar todas las dependencias del archivo requirements.txt en la imagen Docker. Despues, copiamos el resto de los archivos del proyecto en el directorio /code que creamos anteriormente.

El paso final será la utilización del comando cmd para inicializar el microservicio, utilizamos Python Project/Main.py para ejecutar el archivo Python en la imagen del Docker e inicializar el proyecto.

Tras la creación del archivo Docker procedimos a su generación, despliegue y subida a Docker Hub utilizando los siguientes comandos:
* Docker image build . -t microservicionews:1.3

Usando este comando especificamos la creación de una imagen Docker basándonos en el directorio en el cual estamos situados y damos como tag a nuestro nombre el nombre de microservicionews con versión 1.3

* Docker container run –-publish 5000:5000 microservicionews:1.3

Este comando se encarga de ejecutar el Docker que especificamos como microservicionews:1.3 y de publicarlo al puerto 5000:5000, que es el puerto por predefinido que estamos utilizando con Python flask.

* Docker login

Realizamos un login en el servidor de Docker hub, con el fin de tener los permisos necesarios para realizar la subida de la imagen al repositorio previamente creado.

* Docker push oscarrubiogarcia/proyectoccdocker:microservicionews

Comando utilizado para subir la imagen especificada como microservicionews al repositorio oscarrubiogarcia/proyectoccdocker. Destacaremos que previamente realizamos el comando Docker tag para cambiar el nombre de nuestro Docker.

Una vez realizados estos comandos obtendríamos la imagen del Docker creado de alpine, en nuestro repositorio de Docker hub. A continuación, desplegaremos nuestro docker en heroku, para hacer esto tendremos que crear un archivo heroku.yml en nuestro proyecto, preferiblemente junto a nuestro archivo Dockerfile.

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

* Heroku stack:set container

Con este comando estableceremos el stack del proyecto de heroku como de tipo container

* Git push heroku master

Finalmente con este comando publicamos todos los cambios realizados en el repositorio en heroku y este desplegara automáticamente la imagen establecida en el dockerfile.

Mostramos a continuación 2 pequeñas capturas demostrando la subida y despliegue con éxito tanto del Docker a Docker hub como del Docker a Heroku.

![Docker]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/DockerHub.jpg )
![Heroku]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Heroku-Docker.jpg )

Se utilizo el tutorial mostrado en [este enlace](https://runnable.com/docker/python/dockerize-your-flask-application) para la recaudación de información relacionada con la construcción del Docker. 

Adicionalmente también fue utilizada la documentación proporcionada por dockerhub y heroku para el correcto despliegue del Docker. 
* [Documentación heroku](https://blog.heroku.com/build-docker-images-heroku-yml)
* [Documentación docker hub](https://docs.docker.com/docker-hub/)
