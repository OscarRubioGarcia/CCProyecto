
# Provisionamiento

## Configuración de Virtual Machine en Azure

Principalmente describiré brevemente el tipo de máquina que estoy buscando para el sistema actual.

La máquina que crear será una sencilla, sin necesidad de procesadores increíblemente potentes y que utiliza un SO con el cual este familiarizado, pues como este será el primer provisionamiento que creare me gustaría realizarlo en una maquina con la cual pudiera verme trabajando en el futuro.

Por ello nos decantaremos por el siguiente SO:

* Sistema Operativo: Ubuntu, cualquier versión medianamente actual (18).

## Proceso de Creación

Inicialmente crearemos una cuenta en azure.com para poder tener acceso a las máquinas virtuales de azure que utilizaremos en el futuro.

Nos aseguraremos la instalación de ansible en nuestro sistema Ubuntu siguiendo las reglas establecidas por su web oficial.

[Enlace a web ansible oficial.](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu)

Por ello realizaremos los siguientes comandos para conseguir tener ansible instalado.

* sudo apt install software-properties-common
* sudo apt-add-repository --yes --update ppa:ansible/ansible
* sudo apt install ansible

Finalmente comprobaremos la instalación utilizando
* ansible --version

Crearemos nuestra máquina virtual de azure mediante su CLI shell. Este shell lo podremos instalar o podremos utilizar su [cliente online.](https://shell.azure.com/bash)

Inicialmente seleccionamos la creación de un lugar de almacenamiento gratuito. Tras la creación ya podremos comenzar a la creación de las máquinas virtuales.

Comenzaremos tal como nos explica el [tutorial de azure.](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/quick-create-cli?toc=/azure/virtual-machines/linux/toc.json)

Creamos un grupo de recursos.

* az group create --name UGRResourceGroup --location westeurope

Tras hacer esto nuestra máquina virtual Ubuntu será creada bajo el nombre de CCVM para el grupo UGRResrouceGroup, usando las credenciales de admin XXX y creando las claves ssh.

```
az vm create \
  --resource-group UGRResourceGroup \
  --name CCVM2 \
  --image UbuntuLTS \
  --admin-username XXX \
  --generate-ssh-keys
```

En nuestro caso la máquina virtual a sido generada con la siguiente dirección ip publica 23.97.156.34.

Escogí la imagen UbuntuLTS debido a que es un OS con el cual estoy familiarizado, pero si fuera a querer cambiar este OS por algún otro solo necesitaría ejecutar el siguiente comando:

* az vm image list --all

Con este comando recibiríamos (tras un rato en espera) la lista completa con sus características de todas las imágenes de OS que azure tiene.

Actualmente utilizaremos el tamaño estándar de la máquina virtual, puesto que nuestro programa a desplegar no debería requerir demasiado procesamiento y debería de ser relativamente ligero.

Si fuéramos a requerir más o menos tamaño para nuestro principalmente utilizaríamos el siguiente comando para comprobar el tipo de maquia que buscamos:

* az vm list-sizes --location westeurope --output table

Tras conseguir un tamaño apropiado podríamos escalar nuestra máquina virtual mediante el siguiente comando:

* az vm resize --resource-group UGRResourceGroup --name CCVM --size Standard_B4ms

Aquí tenemos un extracto del listado mostrado:

![Foto Tabla resultados.](https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/AzureSizes.jpg)

Tras un breve periodo de tiempo nuestra máquina virtual será creada y podremos comprobar su funcionamiento de la siguiente forma.

* az vm open-port --port 80 --resource-group UGRResourceGroup --name CCVM

Con este comando abriremos el puerto 80 que pretendemos usar en conjunto con nginx tanto para poder observar la máquina virtual creada como el sistema una vez este haya sido desplegado y configurado en conjunto a nginx.

A partir de este punto deberemos acceder a la máquina virtual y empezar la instalación de todos los programas necesarios para el despliegue correcto de nuestro sistema. Para conseguir esto recurriremos al uso del software ansible.

## Ansible

Tras la instalación de ansible en el sistema podemos comenzar a desarrollar playbooks para nuestra máquina virtual.

Principalmente indicaremos al archivo hosts de ansible el servidor web que queremos provisionar. Adicionalmente, podremos asignarle un nombre especifico el cual usaremos para dirigirnos a esa VM, en nuestro caso usaremos webservers.

```
[webservers]
23.97.156.34
```

Comprobamos que el fichero a sido configurado correctamente y que nuestra conexion con el servidor via ssh es correcta mediante:

* ansible all -m ping -u XXX

Para la ejecucion de playbooks utilizaremos el comando:

* ansible-playbook testplaybook.yml

Crearemos un rol para nuestros playbooks comunes, de esta manera si necesitamos reutilizar este rol con otras maquinas virtuales podremos realizarlo de manera simple y facil.

* ansible-galaxy init role

Para la instalación de cassandra daremos uso de ansible-galaxy, de esta forma nos descargaremos el rol encargado de la instalación de cassadnra para nuestra máquina virtual.

* ansible-galaxy install cowops.debian-cassandra

** Debido a problemas con el uso del rol provisto de ansible-galaxy, se decidió crear un rol propio que se encargara de cassandra manualmente.**

### Archivo de provisionamiento basico

#### **core.yml**

```
---

- import_playbook: pythonCheck.yml

- hosts: webservers
  user: XXX
  roles: 
    - { role: cassandra-3.11.4 }
  tasks:
    # Core Programs to be Installed
    - name: Instalacion de programas basicos.
      become: yes
      action: apt pkg={{ item }} state=latest
      loop:
        - python3
        - build-essential
        - libssl-dev
        - libffi-dev
        - python-dev
        - python3-pip
        - python-pip
        - bash
        - git
		- nginx
```

En este primer archivo de provisionamiento nos dedicamos a la instalación principalmente del software que consideramos común entre nuestros microservicios, aunque si fuera a ser necesario utilizar una base de datos diferente entre nuestros microservicios, se podría eliminar la incorporación del rol "cassandra".

Utilizamos un loop para realizar la instalación de múltiples programas. Adicionalmente utilizamos become: yes para realizar estos comandos como superusuario.

En este primer script usamos apt para la instalación de python3 y los paquetes necesarios para la instalación de pip3, estos siendo build-essential, libssl-dev, libffi-dev y python-dev. Finalmente instalamos python3-pip y python-pip por si pip3 no fuera a funcionar en alguna situación.

Instalamos git y bash debido a que son programas que nos serán de gran uso en el futuro, git para la descarga del microservicio y bash por si fuéramos a necesitar ejecutar pequeños scripts.

Inicialmente utilizamos **import_playbook: pythonCheck.yml** para incorporar otro script de provisionamiento a este, el cual realiza una comprobación e instalación de python2.7 si este no fuera a estar instalado en el sistema.

Podemos ver el archivo a continuación:

#### **pythonCheck.yml**
```
---
- hosts: webservers
  user: XXX
  gather_facts: false

  tasks:
    - name: Check for the existence of python 2
      raw: test -e /usr/bin/python
      changed_when: false
      failed_when: false
      register: check_python

    # Install 
    - name: Install Python if it doesnt exist
      raw: apt -y update && apt install -y python-minimal
      when: check_python.rc != 0
```

En este archivo como hemos descrito anteriormente, nos aseguramos de que para nuestro host webservers, el usuario XXX realiza la comprobación de la existencia de python 2 en el sistema y si este no fuera a estar instalado lo instala. Realizamos este paso anterior a todos los demás debido a que si no fuera a estar instalado es posible que esto nos llevara a errores.

La primera tarea se asegurar de comprobar mediante el "test" si python existe en nuestro sistema. Registra este valor el la variable check_python que especificamos.

La segunda tarea se encarga de instalar python 2 solo si este no fue encontrado en el sistema anteriormente. Realiza esta comprobacion mediante el registro check_python.

Realizamos la tarea de la instalación de python mediante el uso de "raw" debido a que es recomendado en la [documentación de ansible.](https://docs.ansible.com/ansible/latest/modules/raw_module.html)

A continuación volvemos al archivo **core.yml**, en el cual especificamos, adicionalmente al host y al usuario, el uso de un rol llamado **cassandra-3.11.4**. Este rol fue creado manualmente con el comando especificado anteriormente y sigue el contiene lo siguiente:

En su carpeta **Files**:

Existen 2 archivos, 1 de ellos siendo la base de datos cassandra-3.11.4 en formato tar.gz y el otro un archivo jvm que será utilizado por la base de datos unas vez la despleguemos en la máquina.

En su carpeta **Tasks**:

#### **main.yml**
```
---
# tasks file for cassandra-3.11.4
- name: Install add-apt-repostory
  become: yes
  apt: 
     name: software-properties-common 
     state: latest

- name: Upgrade and Update 
  become: yes
  apt:
     upgrade: yes
     update_cache: yes

- name: Install Open jdk 8
  become: yes
  apt: 
     name: openjdk-8-jdk
     state: latest

- name: Install certificates
  become: yes
  apt: 
     name: ca-certificates
     state: latest

- name: Install Open jdk jre 8
  become: yes
  apt: 
     name: openjdk-8-jre
     state: latest

- name: Set the correct java version as selected
  become: yes
  alternatives:
     name: java
     path: /usr/lib/jvm/java-1.8.0-openjdk-amd64/bin/java

- name: Copy Cassandra tar
  copy:
     src: apache-cassandra-3.11.4-bin.tar.gz
     dest: /tmp/apache-cassandra-3.11.4-bin.tar.gz

- name: Extract Cassandra
  command: tar -xvf /tmp/apache-cassandra-3.11.4-bin.tar.gz

- name: Copy jvm fix file in Cassandra
  copy:
     src: jvm.options
     dest: /home/XXX/apache-cassandra-3.11.4/conf/

- name: Update 
  become: yes
  apt:
     update_cache: yes
```

Este archivo es bastante auto explicativo, básicamente realizamos todos los pasos necesarios para garantizar la correcta instalación de cassandra. Tenemos especial cuidado durante la instalación de openjdk-8 específicamente debido a que cassandra tiene problemas con iteraciones futuras de este software. 

* Las primeras 5 tareas simplemente instalan paquetes necesarios para el despliegue de cassandra o actualizan los paquetes del sistema. Estos paquetes son software-properties-common (para el posible uso de ppas), openjdk-8-jdk, ca-certificates y openjdk-8-jre.

* La siguiente tarea se encarga de comprobar que la VM asignada en el SO sea opensdk-8. Queremos específicamente esta versión debido a problemas de compatibilidad de cassandra con otras.

* Las ultimas 4 tareas se encargan de la copia de cassandra, extracción de cassandra, reemplazo del archivo jvm en la base de datos cassandra y actualización final de paquetes del sistema.

Las actualizaciones que realizamos durante el script se deben a que los servicios cloud necesitan actualizar su cache manualmente para poder identificar paquetes que posiblemente no hubieran identificado anteriormente.

Utilizamos los 2 archivos especificados en la carpeta de **Files**, de esta manera aseguramos que siempre va a poder ser desplegable el servidor de cassandra, utilizando nuestro fichero jvm personalizado.

#### **newsApp.yml**

```
---

- import_playbook: core.yml

- hosts: webservers
  user: XXX

  tasks:
    - name: Crear directorio CCProyecto
      become: yes
      file:
        path: /CCProyecto
        state: directory
        mode: '0755'

    # Download microservice 1 (News) from github
    - name: Descarga de microservicio 1 (News) de Github.
      become: yes
      git: 
        repo: https://github.com/OscarRubioGarcia/CCProyecto.git
        version: master
        dest: /CCProyecto

    - name: Install virtualenv via pip
      pip:
        name: virtualenv
        executable: pip3
      become: yes
      become_user: root

    - name: Instalar requisitos del App.
      become: yes
      pip: 
        requirements: /CCProyecto/requirements.txt
        virtualenv: /CCProyecto/venv
		
    - name: Copy file to folder
      copy: 
        src: /home/oscar/Desktop/scripts/activateVenvAndDeploy
        dest: /home/XXX/CCProyecto/activateVenvAndDeploy
      become: yes

    - name: Give permissions to file
      file:
        dest: /home/XXX/CCProyecto/activateVenvAndDeploy
        mode: a+x
      become: yes

    - name: Initialize App News
      shell: ./activateVenvAndDeploy
      args:
        chdir: /home/XXX/CCProyecto
      become: yes

```

Este último archivo de provisionamiento sería el encargado de realizar los pasos exclusivos de nuestro microservicio de noticias. Estos pasos serian la creación del directorio si este no existiera, el clonado del microservicio al directorio, la instalación del entorno virtual en el directorio y la instalación de los requisitos específicos en este entorno virtual. 

Resaltaremos el uso de **import_playbook: core.yml** una vez más, esta vez será para encadenar el playbook creado anteriormente (core.yml) junto con este, asegurando la instalación de todos los paquetes básicos.

Las tareas de este script serán definidas a continuación:

* La primera tarea utiliza "become: yes" con el fin de tener los permisos necesarios para crear un nuevo directorio donde guardaremos nuestro microservicio. Se utilizo la [documentación de ansible.](https://docs.ansible.com/ansible/latest/modules/file_module.html)

* La segunda tarea realiza la descarga del repositorio donde se encuentra nuestro microservicio en github al directorio especificado.

* La tercera tarea se encarga de la instalación del entorno virtual mediante pip3 y utilizando permisos de root. Es posible que esta tarea pueda de ser realizada en el script **core.yml** en vez de en este.

* La cuarta tarea se encarga de la instalación de todos los paquetes y librerías especificadas en el requirements.txt de nuestro proyecto. Estos requisitos son instalados en el directorio especificado. Se siguió la [documentación oficial de ansible.](https://docs.ansible.com/ansible/latest/modules/pip_module.html)

* Las ultimas tareas se encargan de copiar el script de inicialización y despliegue del web service. Simplemente copian el archivo del ordenador host al remoto, le incorporan los permisos necesarios y finalmente lo ejecutan.

En un futuro se podría limpiar aquellos archivos creados al clonar el repositorio en la máquina virtual, pues no son todos los archivos clonados necesarios.

## Despliegue

A continuación tendríamos nuestra máquina virtual ya provisionada y lista para ser desplegada.

Para la realización del despliegue se requeriría principalmente iniciar la base de datos cassandra, posiblemente con un daemon en systemd.

** Actualmente el proceso de conversión de cassandra a un daemon no fue posible realizar**

Tras iniciar la base de datos, el sistema debería de poder ser inicializado mediante la activación del entorno virtual y la llamada de invoke runGunicornAsyncParams. Con el fin de automatizar este apartado, el archivo activateVenvAndDeploy fue creado. Este archivo es ejecutado durante el provisionamiento para lanzar el servidor automáticamente una vez termine todo. Este archivo también obtiene los permisos necesarios para su ejecución una vez se termine el provisionamiento.

Se realizaron por lo tanto pruebas utilizando Taurus para poder medir las capacidades de la máquina actual. Estos test fueron realizados en el propio servidor local con el objetivo de llegar a obtener prestaciones similares a los resultados encontrados en el servidor local de nuestra propia máquina.

Se realizo un test Taurus básico utilizado anteriormente:

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
    - http://localhost:5000/news
    - http://localhost:5000/status

reporting:
- final-stats
- console
- blazemeter
```

Los resultados obtenidos de este test fueron los siguientes:

![Foto resultados.](https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/TaurusVM/Test_only_local.png)

Estos resultados nos confirman que el servidor actual contiene capacidades similares a nuestra propia máquina, por lo que podemos asumir que cumplirá correctamente con su funcionamiento. Sin embargo si fuera a querer mejorarse el servidor, se debería de intentar mejorar el código interno y el numero de clusters de cassandra, tras lo cual se podría empezar a plantear la idea de mejorar las prestaciones de nuestra maquina remota. Estas prestaciones podrían ser un numero de núcleos mayor, mejora en la memoria ram o incluso un sistema operativo mas ligero del que estamos utilizando o incluso especializado en funciones de servidor.

## Documentación

Se utilizaron los tutoriales de Azure promovidos en su página [oficial.](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/tutorial-manage-vm)

Para la instalación de Python en ansible se consulto el siguiente [enlace.]( https://relativkreativ.at/articles/how-to-install-python-with-ansible)

Se siguió esta [guía]( https://attacomsian.com/blog/change-default-java-version-ubuntu) para la instalación de openjdk8 y el siguiente [link]( https://docs.ansible.com/ansible/2.4/alternatives_module.html) para la configuración de versiones en ansible.

Se siguió inicialmente esta [guía]( https://blog.deiser.com/es/primeros-pasos-con-ansible) para la comprensión inicial de ansible.

Se consulto la [web oficial de ansbile]( https://docs.ansible.com/ansible/latest/modules/git_module.html), para el desarrollo del script de descarga de git.
