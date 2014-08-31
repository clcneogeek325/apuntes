#!/bin/bash


#====================================
# para instalar un proyecto de django
# debemos de copiar el proyecto y ponerlo en 
# ===================================


/var/www/ # en esta  ruta
/var/www/nombre_de_mi_proyecto/ # quedando asi

# y luego agregarle estas lineas al archivo wsgi.py
# en la cual le decimos que agrege a nuestro proyecto en el path de python


import sys
sys.path.append("/var/www/nombre_de_mi_proyecto/") # ruta de nuestro proyecto
sys.path.append("/home/usuario/nombre_de_mi_entorno_virtual/") # en caso de que vayamos a usar un vistualenv
                                                    # es lo mas recomendable

# reemplazar la configuaracion de app.conf por la nuestra
# y copiarla a 


/etc/apache2/sites-aviable/ 

cd /etc/apache2/sites-aviable/ 

a2enssite app.conf 

service apache2 restart




