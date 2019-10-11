# CCProyecto TuIdea

## Descripción del proyecto

La aplicación en si será una aplicación de ocio con la que el usuario podrá decidir si le gustan o no le gustan las ideas que son mostradas en la aplicación. Por decirlo de alguna forma será un Tinder para ideas. De esta forma el usuario podrá buscar ideas de algún tipo en una base de datos y decidir si estas ideas le gustan o no le gustan. Los votos de los usuarios serán transmitidos a la base de datos y almacenados para poder saber que tipo de ideas son las populares.
Esta aplicación contendrá las siguientes facultades:
 * Inicio de sesión utilizando usuario y contraseña.
 * Búsqueda en la base de datos de ideas categorizadas por tipo y popularidad
 * Historial de ideas en las que el usuario haya buscado
 
Planeamos utilizar Java como lenguaje para la aplicación y en conjunto con Spring boot, Heroku y Maven para poder desplegarlo en la web con posibilidad a escalabilidad. Adicionalmente daremos uso de una base de datos NoSQL y utiilzaremos un servicio REST como nucleo para realizar los servicios maás simples.

## La Arquiectura de los Microservicios

Nuestro proyecto dará uso de la arquitectura de los microservicios de forma de que cada servicio especificado sea independiente del resto de la aplicación, por ejemplo nuestra base de datos se encargara del almacenado de los datos, mientras que heroku y maven serán utilizados para manejar el despliegue de la aplicación y nuestro api REST será la encargada de notificar las acciones realizadas en la aplicación.

## Licencia

El proyecto será generado con una licencia de tipo MIT. Esta licencia no impone muchas limitaciones sobre la reutilización y adicionalmente es altamente compatible con otras licencias como la GNU. Utilizando esta licencia creemos que es posible que no existan problemas a la hora de compartir software.

