# Cambios previos a la experimentación

Con el objetivo de poder desplegar correctamente el microservicio de noticias fue necesario realizar ciertos cambios al código del sistema con el fin de que este pudiera dar uso de nuestra base de datos Cassandra. 

## Cambios en el código

Inicialmente se realizado un cambio general de la estructura que estaba siendo utilizado en Python flask, cambiando el uso de resources por el uso de blueprints. Utilizando este sistema pretendemos organizar mucho mejor los servicio que nuestro sistema proporcionara.

Enlace a la documentacion de [blueprints.](https://flask.palletsprojects.com/en/1.0.x/blueprints/)

Para la correcta implementación del Cache a nuestro sistema y conseguir evitar las referencias circulares en nuestro código se requirió de la creación de la clase Cache, la cual esta encargada de ser el punto de acceso para nuestros blueprints con el fin de utilizar el cache de la app.

Previamente a la comprobación del servicio prestado con Taurus, se incorporo un sistema de cache en el microservicio, proporcionado por Flask-Caching. Utilizando este servicio esperamos conseguir una mejora a la hora de servir servicios similares a los clientes.

Enlace a documentacion de [flask-caching](https://flask-caching.readthedocs.io/en/latest/)

Adicionalmente a lo comentado se preparo toda la estructura de los servicios para acoger el sistema cqlengine de cassandra y su driver. Esto implico la inyección de dependencias en el modelo creado y el uso de estas nuevas funcionalidades. Se creo la clase Base de la cual extenderá nuestro modelo con el fin de poder utilizar correctamente estas funcionalidades y poder mappear nuestro modelo en la BD Cassandra. 

Se creo un punto de inicio en nuestro sistema, este siendo CassandraLaunch.py, desde el cual se iniciara la comunicación con la base de datos y se establecerá su conexión. 

Finalmente, se creo el archivo Generator.py el cual está encargado de la generación de las tablas y la población inicial de estas en la base de datos Cassandra. 

La base de datos cassandra se estableció como una base de datos con 1 único nodo inicialmente, aunque esto podría ser aumentado. Adicionalmente se modificaron los parámetros del archivo cassandra.yaml “read_request_timeout_in_ms: 10000” y “write_request_timeout_in_ms: 20000”, asegurándonos de esta manera que los clusters no se cerrarían a nuestras peticiones demasiado pronto.

Enlace a la documentación del [driver de cassandra cqlengine.]( https://docs.datastax.com/en/drivers/python/2.5/api/cassandra/cqlengine/query.html)

Un ultimo detalle que especificaremos será el uso tanto en gunicorn como en waitress, nuestro sistema de prueba en Windows, de threads. De esta forma en gunicorn estableceremos el uso de 5 workers (como es recomendado 2*(n-cores) +1) con 25 threads y en waitress simplemente estableceremos las 25 threads.

Enlace a la documentación de [gunicorn]( https://docs.gunicorn.org/en/stable/design.html) y [waitress.]( https://docs.pylonsproject.org/projects/waitress/en/stable/arguments.html)

# Experimentación con Taurus

Nuestro objetivo principal con esta experimentación será de conseguir que nuestro sistema pueda soportar un mínimo de 1000 peticiones de 10 usuarios durante varios segundos.

Utilizaremos la herramienta Taurus obtenible [aquí ]( https://gettaurus.org/ ) para realizar la creación de estos Benchmarks.

Principalmente estableceremos que cassandra es una base de datos la cual no esta diseñada para el borrado de datos, haciendo este tipo de servicio muy costos. Esto no debería impedir nuestros tests debido a que nuestro servicio no tiene el interés de borrar archivos muy comúnmente. Debido a esto excluiremos este tipo de servicio de nuestros tests.

Se realizaron diversos scripts probando diversas configuraciones de prueba en Taurus, si se desea ver algunas de estas configuraciones siga el siguiente [enlace.]( https://github.com/OscarRubioGarcia/CCProyecto/tree/master/TaurusTests) Nosotros nos centraremos en este documento solo en aquellos tests que consideramos finales.

Realizamos los principales tests de Taurus con el siguiente script:

```
execution:
- concurrency: 10
  ramp-up: 10s
  hold-for: 60s
  throughput: 1000
  steps: 10
  scenario: basic-services-test

scenarios:
  basic-services-test:
    requests:
    - http://localhost:5000/news
    - http://localhost:5000/status

reporting:
- final-stats
- console
- blazemeter
```

Este archivo fue llamado [only_stats.yml]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/TaurusTests/only_stats.yml)

Este archivo .yml la estructura básica que utilizaremos para la realización de nuestro tests. En este caso definiremos exactamente que ocurre en cada línea de código del test.

---	     <- Estas 3 líneas definirán el comienzo de un test.

Execution: <- Este apartado definirá las reglas que estableceremos a la ejecución del test.

-concurrency: 10 <- Aquí estamos estableciendo a 10 usuarios que actuaran concurrentemente en nuestro test.

ramp-up:10s <- especificamos que queremos que el numero de usuarios vaya incrementando hasta llegar a su número máximo durante los primeros 10 segundos. Escogimos 10 segundos puesto que es una buena métrica para 10 usuarios, siendo 1 por segundo.

Hold-for: 60s <- Establecemos que queremos que nuestro test se mantenga activa durante 60s, siendo en total 50s a potencia máxima.

Throughtput:1000 <- Especificamos que nuestro test no sobrepase las 1000 peticiones por segundo, y se mantenga en ese límite.

Steps:10 <- Aunque no se notara demasiado, establecemos que queremos que nuestro ramp-up vaya en escalones.

 scenario: basic-services-test <- Especificamos el nombre del scenario que ejecutaremos.

 scenarios: <- Establecemos el inicio del bloque de escenarios a diseñar.

 basic-services-test: <- Estableceremos el nombre de nuestro escenario a realizar.


 requests: <- Estableceremos las requests que serán realizadas en el test por los usuarios.

 - http://localhost:5000/news <- Aquí pediremos a nuestro sistema el listado completo de todas las noticias en nuestra BD.

 - http://localhost:5000/status <- En esta llamada pediremos a nuestro sistema su estado actual.

 reporting: <- Indicamos el inicio del bloque de reporting a diseñar

 - final-stats <- Especificamos que queremos que Taurus nos muestre las estadísticas finales del test.

 - console <- Especificamos que queremos que Taurus nos muestre la consola propia con la cual poder visualizar el avance de los tests. 

 - blazemeter <- Indicamos a Taurus que queremos dar uso de sus servicios de visualización de tests web como usuario anónimo. De esta forma conseguiremos los diagramas mostrados a continuación.

Enlace a la información relacionada con los parámetros de [Taurus]( https://gettaurus.org/docs/ExecutionSettings/)

![imagen Taurus vista](https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Taurus/Taurus_test_only_view.png)

En la imagen superior podemos comprobar que nuestro servicio es capaz de mantener 1000 peticiones durante aproximadamente > 25 segundos. En un mundo ideal, estas serian las funcionalidades que más serian accedidas en nuestro sistema, pero en nuestro caso probaremos más situaciones en nuestro sistema.

Este seria el esquema de nuestro test de Taurus .yml  el cual comprobara las introducciones y eliminaciones en nuestra BD. Esperamos tener una gran diferencia entre el tiempo de espera de las eliminaciones comparadas con las inserciones.

```
---
execution:
- concurrency: 10
  ramp-up: 10s
  hold-for: 60s
  throughput: 1000
  steps: 10
  scenario: basic-services-test

scenarios:
  basic-services-test:
    requests:
    - url: http://localhost:5000/news/addById
      method: POST
      headers:
          Content-Type: application/json
      body-file: json_add_specific_news.json
    - url: http://localhost:5000/news/deleteById
      method: DELETE
      headers:
          Content-Type: application/json
      body-file: json_del_news.json

reporting:
- final-stats
- console
- blazemeter
```

Este archivo fue nombrado [test_only_news_add_delete.yml]( https://github.com/OscarRubioGarcia/CCProyecto/blob/master/TaurusTests/test_only_news_add_delete.yml)

El archive sigue el mismo patron descrito anteriormente, pero en este caso contiene unos requests que el anterior no tenía:

```
- url: http://localhost:5000/news/addById
      method: POST
      headers:
          Content-Type: application/json
      body-file: json_add_specific_news.json
```
Este apartado básicamente especifica que la petición utilizara la url específica, que en nuestro caso será la de inserción de datos, utilizara el método POST con los headers de tipo json para enviar como cuerpo el contenido del archivo json_add_specific_news.json. 
Adicionalmente la siguiente petición realizara algo muy similar, cambiando esta vez el método a DELETE y el cuerpo de la petición por otro archivo diferente. 
Estos serán nuestros resultados esta vez:

![imagen Taurus vista](https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/Taurus/Taurus_test_only_add_delete.png)

Como podemos observar, existe una gran diferencia entre los tiempos de respuesta de la adición y de la eliminación. Sera por esto que en nuestra BD se pretenderá nunca eliminar datos si es posible.

Posibles mejoras que se podrían realizar en el sistema serian la incorporación de un sistema de threads internamente para manejar de manera asynchrona tareas pesadas como la eliminación de datos o la recolección de datos cuando las cantidades de estos son grandes. La inclusión de nodos extra a la base de datos cassandra también podría de ser realizado para intentar conseguir una mejora de tiempo de respuesta e evitar que un nodo se ahogue en peticiones.

Se realizo el archivo test_only_news_all.yml adicionalmente como un test más completo de todos lo especificado anteriormente. Usaremos este test como ejemplo principal de todo lo experimentado con Taurus.

```
---
execution:
- concurrency: 10
  ramp-up: 10s
  hold-for: 60s
  throughput: 1000
  steps: 10
  scenario: basic-services-test

scenarios:
  basic-services-test:
    requests:
    - url: http://localhost:5000/news/addById
      method: POST
      headers:
          Content-Type: application/json
      body-file: json_add_specific_news.json
    - http://localhost:5000/status
    - http://localhost:5000/news
    - url: http://localhost:5000/news/findById
      method: POST
      headers:
          Content-Type: application/json
      body-file: json_del_news.json
    - url: http://localhost:5000/news/deleteById
      method: DELETE
      headers:
          Content-Type: application/json
      body-file: json_del_news.json

reporting:
- final-stats
- console
- blazemeter 
```

[Enlace al archivo test_only_news_all.yml](https://github.com/OscarRubioGarcia/CCProyecto/blob/master/TaurusTests/test_only_news_all.yml)

## Archivos de datos diseñados para trabajar junto con Taurus

Json_add_news.json

```

{
	"titulo": " Algo ocurre aqui",
	"descripcion": "Descripcion de test!",
	"campus": "UGR"
}
```

Json_add_specific_news.json

```
{
	"id": "cef0cbf3-6458-4f13-a418-ee4d7e7505dd",
	"titulo": " Algo ocurre aqui",
	"descripcion": "Descripcion de test!",
	"campus": "UGR"
}
```

Json_del_news.json

```
{
	"id": "cef0cbf3-6458-4f13-a418-ee4d7e7505dd"
}
```

Json_add_comment.json

```
{
	"cuerpo": "Comentario test",
	"usuario": "Usuario test",
	"puntuacion": "100",
	"idnoticia": "cef0cbf3-6458-4f13-a418-ee4d7e7505dd"
}
```
