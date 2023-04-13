from io import open_code
import pathlib


archivo = str(pathlib.Path().absolute()) + '/prueba.txt'
leer_archivo = open(archivo, 'r')


leer = leer_archivo.readlines()
for contenido in leer:
    print(contenido.upper())