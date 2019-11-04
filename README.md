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

[Descripción del fichero tasks.py]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/DefinicionTasks.md )

## Despliegue del proyecto

Téngase en cuenta que este proyecto fue diseñado utilizando el software PyCharm para su creación y su testing local.

Para el correcto funcionamiento del proyecto se deberá tener en cuenta todas las librerías especificadas en "requirements.txt" y se deberá tener una versión valida de Python instalada en el sistema (Para más información de las versiones de Python validas, véase el archivo de pruebas “.travis.yml”).

## Historias de Usuario

Para obtener más información acerca de las historias de usuario desarrolladas para este proyecto visite el siguiente enlace: 
[Historias de Usuario]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/UserStories.md )

## Licencia

El proyecto será generado con una licencia de tipo GNU. Esta licencia no impone muchas limitaciones sobre la reutilización. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.
