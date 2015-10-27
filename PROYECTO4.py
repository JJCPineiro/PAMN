# -*- coding: utf-8 -*-
#Paquetes a utilizar en el programa
import os
import json
import requests
import codecs

print '------------INICIO------------'

#Creacion de archivo HTML
archivo = codecs.open("Tarea4.html", "w", 'utf-8')
vacio = ""
archivo.write(vacio)

#Color de fondo para la pagina HTML
fondo = "<meta charset=\"UTF-8\">\n<body bgcolor=Teal>"
#Títular de la página
titulo = "<CENTER>\n<h1>API SPOTIFY</h1>\n</CENTER>"
#Apertura de tablas
tabla_inicio = "<TABLE BORDER=1>"
#Cierre de tablas
tabla_fin = "</TABLE>"
archivo.write(fondo + titulo +  "<CENTER>" + tabla_inicio)

#Lista de amigos 
friends = ["crashbito", "quique_06i", "soloalbertog", "jjcpineiro"]

#Lista de url's
url_A=[]
url_P=[]
url_T=[]

#Token
#""""AQUÍ INGRESE SU TOKEN""" (Después de 'Bearer...')
headers = {'Authorization' : 'Bearer BQDOcZLNDx2SgsRPy10VGQn9ZhKWIZgAKwYnfi2QCxaNMYypX4lydbxjyjmnsxQBHANKMrP3SCsOZNxiRIwtIlcgjDNhSm8byXNIdIsLKMIavBDLxSC6dI_9vesu2n_KkMTWi_ZDb1aorPDPZ_ZcPIsv1Cgh4z6UH4GwplALWmP7tE8Gz_MTi84'}

#Creando url's
for amigo in friends:
	print "Creando url de:  " + amigo
	liga_amigo = "https://api.spotify.com/v1/users/" + amigo
	url_A.append(liga_amigo)
	print "Obteniendo URL playlist de:  " + amigo
	liga_playlist ="https://api.spotify.com/v1/users/" + amigo +"/playlists?offset=0&limit=3"
	url_P.append(liga_playlist)

for i in range (0,4):
#Esperando respuesta
	respuesta = requests.get(url_A[i])

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
	datos = "\n" + "<TR><TD>" + imagen + usuario + id + seguidores + "</TD>"
	archivo.write(datos)
#Pidiendo a Spotify, solicitud para obtener playlists
	respuesta = requests.get(url_P[i],headers=headers)
	playlist = json.loads(respuesta.text)

#Creando nuevo columna y tabla 2
	listas_inicio = "<TD><CENTER><h2>" + "PLAYLISTS</h2>" + tabla_inicio 
	archivo.write(listas_inicio)

#Llenando tabla 2 (interior)
	for j in range(len(playlist['items'])):
		playlist_imagen = "<center><img src='" + playlist['items'][j]['images'][0]['url'] + "' height = 200 width = 200/></center>"
		playlist_nombre = "<center><h3>" + playlist['items'][j]['name'] + "</h3></center>"
		playlist_datos = "<TD>" + playlist_imagen + playlist_nombre + "</TD>"
		archivo.write(playlist_datos)

#Cerrando tabla 2
	listas_fin = tabla_fin + "</TR></CENTER>"

	archivo.write(listas_fin)

#Cerrando tabla general
archivo.write(tabla_fin)
#Cerrando centrado de tabla general
archivo.write("/<CENTER>")

#Cerrando archivo
archivo.close()

#Ejecutando el archivo (html)
os.startfile("Tarea4.html")

print '------------FIN------------'
