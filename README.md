[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

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

Debido a las reglas establecidas por la arquitectura de microservicios tendremos que asegurarnos que todos nuestros servicios sean independientes del resto de la aplicación. Cada servicio tendrá acceso solamente a su base de datos específica y podrán ser testeados de manera aislada. 

Dicho esto crearemos en nuestro proyecto, tendremos APIs REST para manejar la comunicación entre todos nuestros microservicios, a través de HTTP. Estos microservicios serán desarrollados usando Python Flask, debido a su facilidad de uso a la hora de creación de productos web.

Utilizaremos una API GATEWAY creada con Nginx para mantener escalabilidad y manejar las llamas a nuestros servicios. Adicionalmente el bot de telegram se comunicara con el Gateway a la hora de comunicarse con los microservicios.

Los microservicios de “Gestión de Clubs”, “Gestión de Noticias” y “Gestión de Comentarios” tendrá establecida una base de datos NoSQL de MongoDB.

Utilizaremos las siguientes tecnologías para los microservicios:
 * Log: LogStash, será utilizado para mantener logs de todos los microservicios y monitorizarlos.
 * Almacenes de datos: Cassandra será usado para almacenar los datos de cada microservicio que lo necesite.
 * Configuración remota: Etcd, será utilizado para guardar la información crítica del sistema.

#### Comunicación entre microservicios

 * “Gestión de Clubs” se comunicara con el microservicio de “Gestión de Comentarios” mediante una API REST.
 * “Gestión de Noticias” se comunicara con el microservicio de “Gestión de Comentarios” mediante una API REST.
 * La API Gateway se comunicara con los 3 microservicios y con el bot de telegram, atendiendo sus peticiones.

#### Porque usamos las tecnologías escogidas 

Utilizaremos las siguientes tecnologías en el proyecto:
 * Python como lenguaje de programación de nuestros microservicios, debido a su lenguaje simple y poco verboso a la hora de la creación de programas sencillos, como el nuestro en este caso.
 * Etcd para la configuración remota debido a que daremos uso de su capacidad de almacenamiento llaves-valor con seguridad incorporada y su servicio de descubrimiento. 
 * Cassandra será utilizado como almacén de datos de nuestros microservicios, esto se debe al carácter de nuestros datos. Nuestro sistema utilizara datos estilo clave-valor y deberá contener el menor tiempo de respuesta posible con el fin de aportar los resultados lo antes posible al cliente. Cassandra nos aportara todas esas cualidades, además de proporcionar escalabilidad lineal a la base de datos del sistema. Adicionalmente, se podrán modificar las tablas de la base de datos en tiempo de ejecución sin bloquear otras actualizaciones o consultas, permitiendo a múltiples usuarios utilizar el sistema sin problemas.
 * Nginx será utilizado para la creación del API GATEWAY por el cual se realizaran las peticiones a los microservicios. Escogimos Nginx por sus capacidades como balanceador de cargas, servidor web/proxy inverso ligero de alto rendimiento, soporte de HTML, con soporte para más de 10000 conexiones simultaneas.
 * LogStash será utilizado como nuestro sistema de monitorización de microservicios y gestión de logs. Apache LogStache funcionara como servidor único de guardado de logs, algo que podría sernos un problema en el futuro, en el cual guardaremos los datos de logs de nuestro sistema. Todos los logs serán encriptados del servidor web al servidor central proporcionando a nuestro sistema seguridad adicional.
 
### Diagrama de microservicios 

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Representacion-microservicios-V0.7.jpg )

### Historias de Usuario

Para obtener más información acerca de las historias de usuario desarrolladas para este proyecto visite el siguiente enlace: [Historias de Usuario]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/docs/UserStories.md )

## Licencia

El proyecto será generado con una licencia de tipo GNU. Esta licencia no impone muchas limitaciones sobre la reutilización. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.
