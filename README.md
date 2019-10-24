[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Descripción del proyecto

Definiremos nuestro sistema en dirigido al ámbito escolar, específicamente a la formación de grupos sociales entre estudiantes de un establecimiento escolar.

La aplicación en si será una aplicación dedicada a ayudar en la creación de grupos de estudiantes, ya sea con un objetivo específico (Completar un proyecto) o simplemente para compartir intereses (Clubs). Intentaremos crear una pequeña aplicación con la cual los estudiantes podrán formar redes sociales entre ellos.

De esta forma el usuario podrá buscar proyectos o clubs en la base de datos y decidir si desea unirse a estos, demostrando de esta manera que tiene interés por el club. Añadiremos también la posibilidad de que un estudiante se exponga al resto, con el objetivo de formar nuevos proyectos/clubs o simplemente conocer gente. Adicionalmente tendremos un bot en Telegram el cual será utilizado para comunicarse con el sistema.

Esta aplicación contendrá inicialmente las siguientes facultades:
 * Gestión de proyectos. 
    * Búsqueda en la base de datos de proyectos.
    * Creación de nuevos proyectos
    * Eliminación de proyectos existentes
    * Modificación de proyectos existentes
 * Búsqueda en la base de datos de clubs.
    * Búsqueda en la base de datos de clubs.
    * Creación de nuevos clubs
    * Eliminación de proyectos clubs
    * Modificación de proyectos clubs
 * Búsqueda en la base de datos de participantes libres.
    * Búsqueda en la base de participantes libres.
    * Creación de nuevos participantes libres
    * Eliminación de proyectos participantes libres
    * Modificación de proyectos participantes libres
 * Bot de Telegram para inicializar los servicios.

### Microservicios planteados

 * Gestión de Proyectos
 * Gestión de Clubs
 * Gestión de Participantes libres

## La Arquitectura de los Microservicios

Debido a las reglas establecidas por la arquitectura de microservicios tendremos que asegurarnos que todos nuestros servicios sean independientes del resto de la aplicación. Cada servicio tendrá acceso solamente a su base de datos específica y podrán ser testeados de manera aislada. 

Dicho esto crearemos en nuestro proyecto, tendremos APIs REST para manejar la comunicación entre todos nuestros microservicios, a través de HTML. Estos microservicios serán desarrollados usando Python Flask, debido a su facilidad de uso a la hora de creación de productos web y debido a que encaja perfectamente con el tipo de arquitectura de microservicios que estamos utilizando.

Utilizaremos una API GATEWAY creada con Amazon API Gateway para mantener escalabilidad y manejar las llamas a servicios. Adicionalmente el bot de telegram se comunicara con el Gateway a la hora de comunicarse con los microservicios.

Cada microservicio tendrá establecida una base de datos NoSQL especifica.

Utilizaremos las siguientes tecnologías para los microservicios:
 * Log: Kibana, será utilizado para mantener logs de todos los microservicios y monitorizarlos.
 * Almacenes de datos: MongoDB o DynamoDB serán usadas para almacenar los datos de cada microservicio.
 * Configuración remota: Etcd, será utilizado para guardar la información crítica del sistema, acceso a bases de datos.

#### Comunicación entre microservicios

Los microservicios serán independientes los unos de los otros y únicamente se comunicaran con sus almacenes de datos pertinentes y la API Gateway.

La API Gateway se comunicara con los 3 microservicios y con el bot de telegram.
 
### Diagrama de microservicios 

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Representacion-microservicios-V0.4.jpg )

## La Base de Datos

Nuestra base de datos de proyectos contendrá simplemente un idProyecto, establecimientoEscolar, titulo, asignatura, descripción, plazasLibres, grupoTelegram.

Nuestra base de datos de participantes libres contendrá idParticipante, establecimientoEscolar, nombre, apellidos, edad, aliasTelegram, interés, ocupación.

Nuestra base de datos de clubs contendrá un idClub, establecimientoEscolar, nombreClub, descripción, plazasLibres, grupoTelegram.


## Licencia

El proyecto será generado con una licencia de tipo GNU. Esta licencia no impone muchas limitaciones sobre la reutilización. Utilizando esta licencia creemos que es posible que no existan impedimentos a la hora de compartir software.
