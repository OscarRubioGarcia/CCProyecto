
# Definición del archivo ``` tasks.py ```
El archivo ```tasks.py``` dará uso de la librería Invoke para poder realizar las tareas definidas en el archivo ```tasks.py``` de manera cómoda desde la consola. Pondremos de ejemplo nuestra tarea clean:
``` python
@task
def clean():
    print("Test clean task!")
```
Esta tarea al ser ejecutada utilizando el comando ``` invoke clean ```, se encargará de imprimir en pantalla el mensaje “Test clean task!”. Obviamente esta tarea solo esta presente como ejemplo de las funcionalidades de Invoke a la hora de ejecutar comandos Shell.

``` python
@task
def testAll(ctx):
    ctx.run("python -m unittest discover tests")
```

Como podemos ver en el código superior, definiremos un Task, utilizando las etiquetas proporcionadas por invoke, para poder ejecutar comandos de manera más fácil. En este ejemplo ejecutaríamos invoke testAll para realizar un testing completo de nuestro proyecto, pero sería posible limitar el alcance y especificar que tests realizar o que código 

En este caso estaríamos dando uso de la función discover de unittest para buscar todos los archivos test definidos en nuestro caso en el fichero tests, pero debido a que el uso de este método no está justificado para este proyecto realizaremos unas llamadas individuales a los tests de nuestro sistema.

``` python
@task
def testAllManual(ctx):
    ctx.run("python -m unittest tests/testNoticiasModel.py tests/test_gestornoticias.py tests/test_api.py")
    

@task
def testNews(ctx):
    ctx.run("python -m unittest tests/testNoticiasModel.py tests/test_gestornoticias.py")


@task
def testNewsApi(ctx):
    ctx.run("python -m unittest tests/test_api.py")
```

Esta sería la forma predilecta que utilizaremos para la realización del testing de nuestro sistema, especificando de esta manera los tests a realizar y pudiendo ejecutarlos independientemente de otros.


``` python
@task
def testAllCoverageManual(ctx):
    ctx.run("coverage run -m unittest tests/testNoticiasModel.py tests/test_gestornoticias.py tests/test_api.py")
 ```
 
Adicionalmente añadiremos una task con la cual podremos saber la cobertura de nuestro proyecto y la cual podremos utilizar en conjunto con travis para automatizar los tests y la cobertura del proyecto.
``` python
@task
def build(ctx):
    ctx.run("python setup.py build")
```

Esta última tarea se encargará de realizar el build de nuestro proyecto, según esta especificado en el archivo ``` setup.py ```.

En un futuro podremos realizar la automatización de la generación de documentación de nuestro proyecto utilizando sphinx, rinohtype y invoke.

Para más información relacionada con unittest: https://docs.python.org/3/library/unittest.html