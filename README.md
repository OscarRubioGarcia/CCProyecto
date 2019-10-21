[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Descripción del proyecto

La aplicación en si será una aplicación de compra con la que el usuario podrá decidir si desea invertir o no en las historias escritas por otros usuarios. Por decirlo de alguna forma será un Patreon de pequeñas historias escritas por usuarios. De esta forma el usuario podrá buscar historias de algún tipo en la base de datos y decidir si desea invertir en estas, demostrando de esta manera que tiene interés en las historias escritas por ese escritor. Adicionalmente el sistema contendrá un bot el cual será utilizado para publicar en Twitter las ultimas historias que tuvieron inversiones en el sistema.
Esta aplicación contendrá inicialmente las siguientes facultades:
 * Inicio de sesión utilizando usuario y contraseña.
 * Búsqueda en la base de datos de historias categorizadas por tipo.
 * Inversión en historias.
 * Bot de Twitter de notificación de nuevas historias prometedoras.
 
## Tecnologías Planteadas

Planeamos utilizar Java como lenguaje para la aplicación en conjunto con Spring boot con Maven y utilizaremos un servidor Eureka para almacenar toda la información de los microservicios. Tendremos un BOT de Twitter, programado en Node.js, que se comunicará con nuestro microservicio de inversiones. Adicionalmente daremos uso de bases de datos NoSQL para el almacenamiento de los datos de las historias e inversiones. Utilizaremos un api REST para comunicar los 2 microservicios (historias y inversiones) a traves de HTML. Utilizaremos el servidor Eureka en conjunto con Zuul para crear la API Gateway. Finalmente pretenderemos utilizar JWT para autorizar el acceso al sistema.

### Microservicios planteados

 * Búsqueda de historias - Java
 * Sistema de inversión en historias - Java
 * Bot de notificación de nuevas historias prometedoras - Node.js

### Diagrama de microservicios 

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Representacion-microservicios-V0.2.jpg )

## La Arquitectura de los Microservicios

Debido a las reglas establecidas por la arquitectura de microservicios tendremos que asegurarnos que todos nuestros servicios sean independientes del resto de la aplicación. Cada servicio tendrá acceso solamente a su base de datos específica y podrán ser testeados de manera aislada. 
Dicho esto tendremos APIs REST para manejar la comunicación entre los servicios de Búsqueda de historias e inversión en historias, a traves de HTML. Utilizaremos una comunicación asíncrona entre el bot de Twitter y el sistema de inversión en historias para manejar la comunicación entre estos.

## La Base de Datos

Nuestra base de datos de historias contendrá simplemente un id, titulo, autor, categoría, imagen, historia.
Nuestra base de datos de historias prometedoras contendra id_historia, categoria_historia, inversionTotal.

## Licencia

El proyecto será generado con una licencia de tipo GNU. Esta licencia no impone muchas limitaciones sobre la reutilización. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.


