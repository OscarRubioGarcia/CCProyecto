
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
def testNoticiasModel(ctx):
    sys.argv.pop()
    main()
	
def main():
    import tests.testNoticiasModel
    import unittest
    unittest.main(module='tests.testNoticiasModel')
```

