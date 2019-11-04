
# Definición del archivo .travis.yml

Principalmente definiremos la estructura actual de nuestro fichero .travis.yml e iremos agregando el extracto del fichero que corresponde al apartado:
 
 * Lenguaje utilizado en el microservicio:
 
    ```
    language: python 
    ```
 
 * Versión del lenguaje que instalar en la máquina virtual de testing
	```
	python:
	- "3.4"      # Earliest branch
	- "3.5"
	- "3.6"      # current default Python on Travis CI
	- "3.7"
	- "3.7.5"
	- "3.8-dev"  # dev build
	```

 * Instalación de dependencias del sistema
 
	```
	install:
	- pip install -r requirements.txt
	```

 * Script para la realización de los tests:
 
	```
    script:
	- python -m unittest discover tests
	```

Ahora definiremos un poco en más detalle, cuando sea posible, porque escogimos las opciones que escogimos en este fichero.

 * Para **el lenguaje**, debido a que nuestros microservicios han sido programados en Python, fue obvio que debíamos especificar Python como nuestro lenguaje de programación.
 * Para **las versiones** del lenguaje escogido, fuimos experimentando con versiones diferentes hasta poder encontrar el rango de versiones validas para nuestro proyecto. En este caso la versión mínima de Python para nuestro proyecto sería la 3.4 y soportaríamos hasta la versión mas novedosa de Python, 3.8-dev.
 * Para **la instalación** de dependencias, debido a que utilizaremos Python damos uso de pip para instalar todas las dependencias de nuestro proyecto, las cuales están guardadas en el archivo requirements.txt.
 * Para **el script** de ejecución de tests, utilizaremos Python para ejecutar todos los scripts de tipo unittest que puedan ser descubiertos en el directorio tests.










