## Descripción del proyecto

<<<<<<< HEAD
La aplicación en si será una aplicación de compra con la que el usuario podrá decidir si desea comprar o no las historias escritas por otros usuarios. Por decirlo de alguna forma será un Patreon para pequeñas historias escritas por los usuarios. De esta forma el usuario podrá buscar historias de algún tipo en la base de datos y decidir si desea invertir en estas, demostrando de esta manera que tiene interés en las historias escritas por ese escritor. Adicionalmente podrá votar positiva o negativamente las historias. Los votos de los usuarios serán transmitidos a la base de datos y almacenados para poder saber qué tipo de historias son las más populares.
Esta aplicación contendrá inicialmente las siguientes facultades:
 * Inicio de sesión utilizando usuario y contraseña.
 * Búsqueda en la base de datos de historias categorizadas por tipo y popularidad.
 * Votación de las historias por parte del usuario (Me gusta / No me gusta).
 * Inversión en historias.
 * Recuento de votos.
 * Sistema de escritores favoritos.
 * Notificación de nuevas historias.
 
## Tecnologías Planteadas

Planeamos utilizar Java como lenguaje para la aplicación en conjunto con Spring boot y utilizaremos Heroku y Maven para poder desplegarlo con escalabilidad en la web. Adicionalmente daremos uso de bases de datos NoSQL para el almacenamiento de los datos de historias y usuarios. Utilizaremos un api REST para cada servicio utilizado en la aplicación y un API como núcleo. JWT será utilizado para autorizar el acceso al sistema.

### Microservicios planteados
=======
La aplicación en si será una aplicación de compra con la que el usuario podrá decidir si desea comprar o no las ideas que son mostradas en la aplicación. Por decirlo de alguna forma será un Ebay para ideas. De esta forma el usuario podrá buscar ideas de algún tipo en una base de datos y decidir si desea invertir en estas ideas. Adicionalmente podrá votas positiva o negativamente las ideas. Los votos de los usuarios serán transmitidos a la base de datos y almacenados para poder saber qué tipo de ideas son las populares.
Esta aplicación contendrá inicialmente las siguientes facultades:
 * Inicio de sesión utilizando usuario y contraseña.
 * Búsqueda en la base de datos de ideas categorizadas por tipo y popularidad.
 * Votación de las ideas por parte del usuario (Me gusta / No me gusta).
 * Compra de ideas.
 * Recuento de votos.
 
Planeamos utilizar Java como lenguaje para la aplicación y en conjunto con Spring boot, Heroku y Maven para poder desplegarlo en la web con posibilidad a escalabilidad. Adicionalmente daremos uso de una base de datos NoSQL para el almacenamiento de los datos y utilizaremos un api REST como núcleo de la aplicación. JWT será utilizado para autorizar el acceso al sistema.

### Microservicios planteados

 * Listado de ideas
 * Compra de ideas

## La Arquitectura de los Microservicios

Nuestro proyecto dará uso de la arquitectura de los microservicios de forma de que cada servicio especificado sea independiente del resto de la aplicación, por ejemplo nuestra base de datos NoSQL se encargara de los servicios relacionados con el almacenamiento/borrado/modificación de datos, mientras que heroku y maven serán utilizados para manejar el despliegue de la aplicación y el balanceo de cargas y nuestro api REST será encargado de notificar las acciones realizadas en la aplicación.

## La Base de Datos

Nuestra base de datos de ideas contendrá simplemente un id, titulo, imagen y suma de votos
>>>>>>> d2ecd05aa1fd95a9f18df4e8284364abe0c12a4c

 * Búsqueda de historias
 * Sistema de inversión en historias
 * Sistema de facturación de compras
 * Sistema de notificación de usuarios
 * Gestión de Inversor
 * Gestión de Escritor
 * Gestión de favoritos

### Diagrama de microservicios 

![Microservicios]( https://github.com/OscarRubioGarcia/CCProyecto/tree/master/docs/Representacion-microservicios.jpg )

## La Arquitectura de los Microservicios

<<<<<<< HEAD
Debido a las reglas establecidas por la arquitectura de microservicios tendremos que asegurarnos que todos nuestros servicios sean independientes del resto de la aplicación. Cada servicio tendrá acceso solamente a su base de datos específica y podrán ser testeados de manera aislada. 

## La Base de Datos

Nuestra base de datos de historias contendrá simplemente un id, titulo, autor, categoría, imagen, historia y suma de votos

## Licencia

El proyecto será generado con una licencia de tipo MIT. Esta licencia no impone muchas limitaciones sobre la reutilización y adicionalmente es altamente compatible con otras licencias como la GNU. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.
=======
El proyecto será generado con una licencia de tipo MIT. Esta licencia no impone muchas limitaciones sobre la reutilización y adicionalmente es altamente compatible con otras licencias como la GNU. Utilizando esta licencia creemos que es posible que no existan problemas a la hora de compartir software.
>>>>>>> d2ecd05aa1fd95a9f18df4e8284364abe0c12a4c
