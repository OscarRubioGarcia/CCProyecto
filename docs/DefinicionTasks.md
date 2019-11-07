
# Definición del archivo ``` tasks.py ```
El archivo ```tasks.py``` dará uso de la librería Invoke para poder realizar las tareas definidas en el archivo ```tasks.py``` de manera cómoda desde la consola. Pondremos de ejemplo nuestra tarea clean:
``` 
@task
def clean():
    print("Test clean task!")
```
Esta tarea al ser ejecutada utilizando el comando ``` invoke clean ```, se encargará de imprimir en pantalla el mensaje “Test clean task!”. Obviamente esta tarea solo esta presente como ejemplo de las funcionalidades de Invoke a la hora de ejecutar comandos Shell.

```
@task
def testAll(ctx):
    ctx.run("python -m unittest discover tests")
```

Como podemos ver en el código superior, definiremos un Task, utilizando las etiquetas proporcionadas por invoke, para poder ejecutar comandos de manera más fácil. En este ejemplo ejecutaríamos invoke testAll para realizar un testing completo de nuestro proyecto, pero sería posible limitar el alcance y especificar que tests realizar o que código 
