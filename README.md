## Descripción del proyecto

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

## Licencia

El proyecto será generado con una licencia de tipo MIT. Esta licencia no impone muchas limitaciones sobre la reutilización y adicionalmente es altamente compatible con otras licencias como la GNU. Utilizando esta licencia creemos que es posible que no existan problemas a la hora de compartir software.
