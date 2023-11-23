# Esport
Backend para página de Esports.
Hasta ahora este proyecto se realiza de manera LOCAL (mismas dependencias para todos los proyectos)
por lo que deberá instalar las mismas versiones de python y django en su ordenador en función de observar los 
mismos resultados, además evitar problemas de compatibilidad.
Hata ahora se ha desarrollado el proyecto con:
- Python 3.10.4
- Django 4.0.5
- La base de datos usada es SQL3 y viene integrada por defecto en Django por lo que no deberá instalar nada respecto a BBDD
- Para craar entorno virtual en mac usar el comando: 
python3 -m venv nombre_del_entorno_virtual
- Activar entorno virtual "esport-django" source esport-django/bin/activate
- Instalar las dependencias del proyecto ejecutando los siguientes comandos:
pip install Django==4.0.5
pip install Pillow
pip install django-crispy-forms
pip install python-decouple

-Para el buen funcionamiento de la carga de imagenes en nuevas APIS instalar en la terminal, pip install Pillow
-Instala pip install django-crispy-forms para el correcto funcionamiento de los formularios 
-Instalar pip install python-decouple para las variables de entorno

Para inicializar el servidor en la terminal y desde el directorio principal 
del proyecto se utiliza la instrucción:
(mac)

python3 manage.py runserver 
 
el proyecto sera accesible desde 
el puerto 8000. Ej: http://127.0.0.1:8000/home/  le dará acceso a la vista principal desde la cual
podrá interactuar con el sitio en general


