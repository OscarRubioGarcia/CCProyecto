[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/OscarRubioGarcia/CCProyecto.svg?branch=master)](https://travis-ci.org/OscarRubioGarcia/CCProyecto)

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

Daremos uso de Invoke como nuestra herramienta de construcción para nuestro proyecto en Python.

buildtool: tasks.py

[Descripción del fichero tasks.py.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/DefinicionTasks.md )

## Framework de Testing Local


Con el fin de mantener la integración de nuevos módulos o cambios en nuestro proyecto, libre de fallos, utilizare el framework unitTest. Con este framework podré definir los pasos necesarios para el correcto testing de cada uno de mis microservicios, asegurándome que durante los “tests” se realizan los procesos de setUp, testing y tearDown correctamente. De esta forma estableceré un sistema de testing local que me permitirá comprobar si mis microservicios siguen siendo funcionales a medida que los incorporo o modifico.

Para más informacion de los tests 
[enlace a la descripción de los tests.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/Tests.md )

## Integración Continua en la Nube

Daremos uso de TravisCI para la integración continua del proyecto en el repositorio. Travis se encargará de instalar todas las librerías y lenguajes de programación que fueran necesarios en nuestro proyecto y realizara los tests desarrollados con unitTest por nosotros. Utilizando TravisCI conseguiremos comprobar el funcionamiento correcto de nuestro tests en diversas versiones de Python y monitorizar los posibles errores que puedan ocurrir. TravisCI al estar montado en la nube será perfecto para nosotros a la hora de utilizarlo para comprobar la integración continua de nuestro sistema de microservicios en la nube.

Para más informacion del archivo .travis.yml 
[enlace a la descripción del fichero .travis.yml.]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/Travis.md )

## Despliegue del proyecto

Téngase en cuenta que este proyecto fue diseñado utilizando el software PyCharm para su creación y su testing local.

Para el correcto funcionamiento del proyecto se deberá tener en cuenta todas las librerías especificadas en "requirements.txt" y se deberá tener una versión valida de Python instalada en el sistema (Para más información de las versiones de Python validas, véase el archivo de pruebas “.travis.yml”).

## Historias de Usuario

Para obtener más información acerca de las historias de usuario desarrolladas para este proyecto visite el siguiente enlace: 
[Historias de Usuario]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/UserStories.md )

## Licencia

El proyecto será generado con una licencia de tipo GNU. Esta licencia no impone muchas limitaciones sobre la reutilización. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.
