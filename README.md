[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Descripción del proyecto

Definiremos nuestro sistema dirigido al ámbito escolar, específicamente a la formación de grupos sociales entre estudiantes de un establecimiento escolar y a la notificación de nuevos clubs o noticias.

La aplicación en si será una aplicación dedicada a ayudar en la creación de grupos de estudiantes y mantenerles informados de noticias ocurriendo en su campus. Intentaremos crear una pequeña aplicación con la cual los estudiantes podrán formar redes sociales entre ellos.

De esta forma el usuario podrá buscar clubs en la base de datos y decidir si desea unirse a estos o simplemente buscar las noticias que estén ocurriendo en el campus. Añadiremos también la posibilidad de que un estudiante se exponga al resto, con el objetivo de formar nuevos clubs o simplemente conocer gente. Existirá también un buscador de novedades en el campus. Adicionalmente tendremos un bot en Telegram el cual será utilizado por los estudiantes para comunicarse con el sistema.

Esta aplicación contendrá inicialmente las siguientes facultades:
* Gestión de clubs. 
* Gestión de noticias.
* Gestión de estudiantes libres.
* Visor de Novedades
* Bot de Telegram para inicializar los servicios.

### Microservicios planteados

 * Gestión de Noticias
 * Gestión de Clubs
 * Gestión de Participantes libres
 * Visor de Novedades

## La Arquitectura de los Microservicios

Debido a las reglas establecidas por la arquitectura de microservicios tendremos que asegurarnos que todos nuestros servicios sean independientes del resto de la aplicación. Cada servicio tendrá acceso solamente a su base de datos específica y podrán ser testeados de manera aislada. 

Dicho esto crearemos en nuestro proyecto, tendremos APIs REST para manejar la comunicación entre todos nuestros microservicios, a través de HTML. Estos microservicios serán desarrollados usando Python Flask, debido a su facilidad de uso a la hora de creación de productos web.

Utilizaremos una API GATEWAY creada con Nginx para mantener escalabilidad y manejar las llamas a servicios. Adicionalmente el bot de telegram se comunicara con el Gateway a la hora de comunicarse con los microservicios.

Los microservicios de “Gestion de Clubs”, “Gestion de Noticias” y “Gestion de Estudiantes Libres” tendrá establecida una base de datos NoSQL de MongoDB.

Utilizaremos las siguientes tecnologías para los microservicios:
 * Log: X, será utilizado para mantener logs de todos los microservicios y monitorizarlos.
 * Almacenes de datos: MongoDB será usado para almacenar los datos de cada microservicio que lo necesite.
 * Configuración remota: Consul, será utilizado para guardar la información crítica del sistema.

#### Comunicación entre microservicios

 * “Gestion de Clubs” se comunicara con el microservicio de “Visor de Novedades” mediante una API REST.
 * “Gestion de Noticias” se comunicara con el microservicio de “Visor de Novedades” mediante una API REST.
 * “Gestion de Estudiantes Libres” se comunicara con el microservicio de “Visor de Novedades” mediante una API REST.
 * La API Gateway se comunicara con los 4 microservicios y con el bot de telegram, atendiendo sus peticiones.

#### Tecnologias Usadas y porque

Utilizaremos las siguientes tecnologías en el proyecto:
 * Python como lenguaje de programación de nuestros microservicios, debido a su lenguaje simple y poco verboso.
 * Consul para la configuración remota debido a que daremos uso de su capacidad de almacenamiento llaves-valor y su servicio de descubrimiento. Adicionalmente podríamos utilizarlo para la monitorización del sistema.
 * MongoDB para ser utilizado como almacén de datos de los microservicios, esto se debe al carácter de nuestros datos. Nuestro sistema no requiere respuestas en tiempo real y solo tratara con datos simples estilo documentos, es por esto por lo que MongoDB, utilizando la flexibilidad del lenguaje JSON, nos será perfecto para nuestro sistema.
 * Nginx será utilizado para la creación del API GATEWAY por el cual se realizaran las peticiones a los microservicios. Escogimos Nginx por sus capacidades como balanceador de cargas, servidor web/proxy inverso ligero de alto rendimiento, soporte de HTML, con soporte para más de 10000 conexiones simultaneas.
 * Sistema logs (X)

 
### Diagrama de microservicios 

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Representacion-microservicios-V0.5.jpg )

## Licencia

El proyecto será generado con una licencia de tipo GNU. Esta licencia no impone muchas limitaciones sobre la reutilización. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.
