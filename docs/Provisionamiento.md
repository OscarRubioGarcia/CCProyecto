
# Provisionamiento

## Configuración de Virtual Machine en Azure

Inicialmente crearemos una cuenta en azure.com para poder tener acceso a las máquinas virtuales de azure que utilizaremos en el futuro.

Nos aseguraremos la instalación de ansible en nuestro sistema Ubuntu siguiendo las reglas establecidas por su web oficial.

[enlace a web ansible oficial.](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu)

Por ello realizaremos los siguientes comandos para conseguir tener ansible instalado.

* sudo apt install software-properties-common
* sudo apt-add-repository --yes --update ppa:ansible/ansible
* sudo apt install ansible

Finalmente comprobaremos la instalación utilizando
* ansible --version

Crearemos nuestra máquina virtual de azure mediante su CLI shell. Este shell lo podremos instalar o podremos utilizar su cliente online.

[cliente online.](https://shell.azure.com/bash)

Inicialmente seleccionamos la creación de un lugar de almacenamiento gratuito. Tras la creación ya podremos comenzar a la creación de las máquinas virtuales.

Comenzaremos tal como nos explica el [tutorial de azure.](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/quick-create-cli?toc=/azure/virtual-machines/linux/toc.json).

Creamos un grupo de recursos.

* az group create --name UGRResourceGroup --location westeurope

Tras hacer esto nuestra máquina virtual Ubuntu será creada bajo el nombre de CCVM para el grupo UGRResrouceGroup, usando las credenciales de admin XXX y creando las claves ssh.

''' python
az vm create \
  --resource-group UGRResourceGroup \
  --name CCVM2 \
  --image UbuntuLTS \
  --admin-username XXX \
  --generate-ssh-keys
'''

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

![Foto Tabla resutlados.](https://raw.githubusercontent.com/OscarRubioGarcia/CCProyecto/master/docs/AzureSizes.jpg)

Tras un breve periodo de tiempo nuestra máquina virtual será creada y podremos comprobar su funcionamiento de la siguiente forma.

* az vm open-port --port 80 --resource-group UGRResourceGroup --name CCVM

Con este comando abriremos el puerto 80 que pretendemos usar en conjunto con nginx tanto para poder observar la máquina virtual creada como el sistema una vez este haya sido desplegado y configurado en conjunto a nginx.

A partir de este punto deberemos acceder a la máquina virtual y empezar la instalación de todos los programas necesarios para el despliegue correcto de nuestro sistema. Para conseguir esto recurriremos al uso del software ansible.

## Ansible

Tras la instalación de ansible en el sistema podemos comenzar a desarrollar playbooks para nuestra máquina virtual.






## Documentación

Se utilizaron los tutoriales de Azure promovidos en su página [oficial.](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/tutorial-manage-vm)
