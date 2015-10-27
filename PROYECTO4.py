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
tracks = []

#Token
#""""AQUÍ INGRESE SU TOKEN""" (Después de 'Bearer...')
headers = {'Authorization' : 'Bearer BQBVYQgQe9o9eodFv3gVpohyNzJsv3g9EL0B4EnEYSvlnUM7noRGluIKgWUldMA6hwxyBjYRXlyZvOqmMPwz0IPQ4iZohSEW5m3_vcmiz0VR9YZGZJYcjC1oWQqOxS4-rNBBnV0IC1d2uEurpx7cCNJXRkj0bpp9Q9cRfruop4tMzFpHaaKMk3I'}

#Creando url's
for amigo in friends:
	print "Creando url de:  " + amigo
	liga_amigo = "https://api.spotify.com/v1/users/" + amigo
	url_A.append(liga_amigo)
	print "Obteniendo URL playlist de:  " + amigo
	liga_playlist ="https://api.spotify.com/v1/users/" + amigo +"/playlists?offset=0&limit=3"
	url_P.append(liga_playlist)

for i in range(len(friends)):
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
		playlist_tracks = playlist['items'][j]['tracks']['href']
		url_T.append(playlist_tracks)
		archivo.write(playlist_datos)

#Cerrando tabla 2
	listas_fin = tabla_fin + "</TR></CENTER>"

	archivo.write(listas_fin)

#Cerrando tabla general
archivo.write(tabla_fin)
#Cerrando centrado de tabla general
archivo.write("/<CENTER>")

#Entrando a las playlists
for i in range(len(url_T)):
	respuesta = requests.get(url_T[i], headers = headers)
	canciones = json.loads(respuesta.text)
	
#Obteniendo canciones de las playlists
	for j in range(len(canciones['items'])):
		track_nombre = canciones['items'][j]['track']['name']
		tracks.append(track_nombre)

conde =  0
#Encontrando el número máximo 
for rola in tracks:
	tracks.sort()
	if (conde < tracks.count(rola)):
		conde = tracks.count(rola)

top = 0
total = 0
top_ten = []
#Elección de canciones "TOP TEN"
while(10>top):
	if(total<=len(tracks)):
		for rola in tracks:
			if(tracks.count(rola)==conde and top<10):
				if rola not in top_ten:
					top_ten.append(rola)
					top += 1
				total += 1
	else:
		total = 0
		conde -= 1

entrada = "<h2>TOP TEN</h2>"
archivo.write(entrada)
for i in range(len(top_ten)):
	music = "<h3>" + "[" + str(i+1) + "]" + top_ten[i] + "</h3>"
	archivo.write(music)

#Cerrando archivo
archivo.close()

#Ejecutando el archivo (html)
os.startfile("Tarea4.html")

print '------------FIN------------'

#Cruz Piñeiro Josué de Jesús
#Gómez Ríos José Alberto
#Pérez Martínez Enrique