# Tutorial de Django: ¡Hola Mundo!

<div align="center">

![Django Framework](./img/Captura%20de%20pantalla%202024-03-15%20193622.png)

</div>

Este tutorial te guiará a través del proceso de construcción de una aplicación web simple que muestra el mensaje **¡Hola Mundo!** en tu navegador utilizando Django.

## Pasos para construir la aplicación "Hola Mundo"

### 1. Configuración inicial del proyecto

Asegúrate de tener instalado Django en tu entorno de desarrollo. Si no lo tienes instalado, puedes instalarlo utilizando pip.

Luego, crea un proyecto Django llamado **HelloWorldDjango** utilizando el comando adecuado.

### 2. Configuración de las rutas

Abre el archivo **urls.py** dentro del directorio **HelloWorldDjango** y agrega una ruta para conectar tu aplicación **mi_app**.

### 3. Creación de la aplicación "mi_app"

Crea una nueva aplicación llamada **mi_app** utilizando el comando adecuado.

Luego, dentro del archivo **mi_app/views.py**, define una función llamada **hello_world** que utilice **HttpResponse** para devolver el mensaje **¡Hola Mundo!**.

### 4. Configuración de las rutas de la aplicación "mi_app"

Crea un archivo llamado **urls.py** dentro del directorio **mi_app**, y define la ruta para la vista **hello_world**.

### 5. Ejecución de la aplicación

Finalmente, ejecuta el servidor de desarrollo de Django utilizando el comando adecuado.

Ahora podrás acceder a la aplicación **Hola Mundo** en tu navegador visitando la URL correspondiente. Deberías ver el mensaje **¡Hola Mundo!** en la página.

### 6. Ejecución de las pruebas

Para asegurarte de que tu aplicación funcione correctamente, ejecuta el comando:

``` bash
python manage.py test mi_app.tests
```