# -*- coding: utf-8 -*-
 
import os
import json
import requests
import codecs

#Entrada de usuario [TEMA]
entrada = raw_input("Que desea buscar?  ")
buscar = entrada.split()
buscar_url = "+".join(buscar) + "+"

#Creando URL de Spotify [API]
url = "https://api.spotify.com/v1/search?q=" + buscar_url + "&type=track"

#Creando URL's
respuesta = requests.get(url)
spotify = json.loads(respuesta.text)

#Obteniendo canciones
if (len(spotify['tracks']['items']) == 0):
	print "\tNO HAY CANCIONES ;( "
else:
	for i in range(len(spotify['tracks']['items'])):	
		print "\t" + spotify['tracks']['items'][i]['name']
