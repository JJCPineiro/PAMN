# -*- encoding: UTF-8 -*-

import os
import json
import requests
import codecs

#~~~~~~~~~~~~~~~~ KEY ~~~~~~~~~~~~~~~~~~
key = "AIzaSyDJQdngeeo-l5cWs6b6i-zJVXEkLDsAK88"

#Creando archivo HTML
archivo = codecs.open("MyApps.html", "w", "utf-8")
vacio = ""
archivo.write(vacio)

#Limpiando pantalla
if(os.name == "nt"):
	os.system("cls")
else:
	os.system("clear")

#Inicio
print ("~~~~~~~~~~~~~~~~~~ MyApps ~~~~~~~~~~~~~~~~~~")
print (" ~~~~~~~~~~~~~~~~ UNAM FI ~~~~~~~~~~~~~~~~~ ")
fondo = "<meta charset=\"UTF-8\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />\n<body>\n"
inicio = "<CENTER><h1>~~~~~~~~~~~~~~~~~~ MyApps ~~~~~~~~~~~~~~~~~~\n</br> ~~~~~~~~~~~~~~~~ UNAM FI ~~~~~~~~~~~~~~~~~ </h1>\n"
tabla_inicio = "<TABLE border = 1><tr>"
archivo.write(fondo + inicio + tabla_inicio)

#Preguntando al usuario
buscar = raw_input("Que desea buscar? \n\n>>")
palabras = buscar.split()
buscar_url = "+".join(palabras)

#Crando URL's
URL_spot = "https://api.spotify.com/v1/search?q=" + buscar_url + "&type=track" #SPOTIFY
URL_you = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + buscar_url + "&key=" + key #YOUTUBE

#Obteniendo canciones [SPOTIFY]
inicio_spot = "\n<td valign=TOP><center><h2>SPOTIFY</h2></center>"
archivo.write(inicio_spot)
respuesta_spot = requests.get(URL_spot)
spotify = json.loads(respuesta_spot.text)
if (len(spotify['tracks']['items'])==0):
	print "NO HAY CANCIONES ;("
else:
	for i in range(len(spotify['tracks']['items'])):
		imagens = "\n<img src=\'" + spotify['tracks']['items'][i]['album']['images'][1]['url'] + "\' />"
		musica = "\n</br><embed src=\"" + spotify['tracks']['items'][i]['preview_url'] + "\" autostar=\"0\" autoplay=\"0\" width=\"300\" height=\"20\">"
		titulo_spot = "\n<h3>" + spotify['tracks']['items'][i]['name'] + "</h3>"
		dato = "<center>" + imagens + musica + titulo_spot + "</center>"
		archivo.write(dato)
fin_spot = "</td>"

#Obteniendo videos [YOUTUBE]
inicio_you = "<td valign=TOP><center><h2>YOUTUBE</h2></center>"
archivo.write(inicio_you)
respuesta_you = requests.get(URL_you)
youtube = json.loads(respuesta_you.text)
if (len(youtube['items']) == 0):
	print "NO HAY VIDEOS ;("
else:
	for i in range(len(youtube['items'])):
		titulo_you = "\n<h3>" + youtube['items'][i]['snippet']['title'] + "</h3>"
		if (youtube['items'][i]['id']['kind'] == "youtube#channel"):
			liga = "http://www.youtube.com/channel/" + youtube['items'][i]['snippet']['channelId']
			enlace = "\n<a href=\"" + liga + "\" target=\"blank\">"
			imageny = "\n<img src=\'" + youtube['items'][i]['snippet']['thumbnails']['medium']['url'] + "\' />"
			dato = "<center>" + enlace + imageny + titulo_you + "</a> </center>"
			archivo.write(dato)
		else:
			liga = "http://www.youtube.com/embed/" + youtube['items'][i]['id']['videoId']
			video = "\n<iframe width=\"640\" height=\"385\" src=\"" + liga + "\" ></iframe>"
			dato = "<center>" + video + titulo_you + "</center>"
			archivo.write(dato)
fin_you = "</td>"
archivo.write(fin_you)

#Fin
print ("\n\t...LISTO...")
fin = "\n</tr></TABLE></CENTER></body>"
archivo.write(fin)

#Cerrando archivo
archivo.close()

#Ejecutando archivo [HTML]
os.startfile("MyApps.html")
