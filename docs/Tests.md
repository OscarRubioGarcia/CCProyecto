

# Descripción de los Tests realizados y su estructura

Tuvimos que instalar coverage con el fin de poder ejecutar nuestros tests utilizando la herramienta de coverage. 
Tras la ejecución de los test y su éxito, ejecutamos un comando bash con el objetivo de notificar a codecov.io de la terminación con éxito de los tests e inicializar la creación del documento de cobertura que será utilizado por codecov para poder darnos la descripción del código cubierto por nuestros tests.

Actualmente hemos realizado 2 tipos de testing sobre los modelos de nuestros microservicios y sobre la API REST. 
Estos 2 tipos de testing han sido tests unitarios, con el fin de comprobar el correcto funcionamiento de los métodos encargados del manejo de nuestros microservicios y tests integración para microservicios. Actualmente solo testeamos un simple servicio REST que no será utilizado en nuestro microsistema final, pero sirve como ejemplo para demostrar los tests de integración de microservicios.

