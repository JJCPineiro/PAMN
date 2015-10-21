# -*- coding: utf-8 -*-
#Paquetes a utilizar en el programa
import os
import json
import requests
import codecs

print '------------INICIO------------'

#Creacion de archivo HTML
archivo = codecs.open("Tarea4.html", "w", 'utf-8')

#Color de fondo para la pagina HTML
fondo = "<meta charset=\"UTF-8\">\n<body bgcolor=Teal>"
archivo.write(fondo)

#Lista de amigos 
friends = ["crashbito", "quique_06i", "soloalbertog", "jjcpineiro"]
#Lista de url's
url=[]

#Creando url's
for amigo in friends:
	print "Creando url de:  " + amigo
	liga = "https://api.spotify.com/v1/users/" + amigo
	url.append(liga)

for i in range (0,4):
#Esperando respuesta
	respuesta = requests.get(url[i])

#Obteniendo el json de cada amigo
	spot = json.loads(respuesta.text)

#Imagen de usuario
	imagen = "<img src='" + spot['images'][0]['url'] + "' />"
#Nombre de usuario
	usuario = "<h2> Nombre de usuario: </h2> <h3>.......... " + spot['display_name'] + "</h3>"
#ID del usuario
	id = "<h2> ID: </h2> <h3>.......... " + spot['id'] + "</h3>"
#followers
	seguidores = "<h2> Followers: </h2> <h3>.......... " + str(spot['followers']['total']) + "</h3>"
#Impresión en archivo -> html
	doc = "\n" + imagen + usuario + id + seguidores
	archivo.write(doc)

#Cerrando archivo
archivo.close()

#Ejecutando el archivo (html)
os.startfile("Tarea4.html")

print '------------FIN------------'
