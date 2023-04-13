from io import open
import pathlib
import shutil
import os

#abrir archivo
#para que pueda encontrar la ruta segura al archivo
#ruta = str(pathlib.Path().absolute()) + '/fichero_texto.txt'
#archivo = open(ruta, 'a+')

#texto = " soy un texto" + '\n'
#archivo.write(texto)
#archivo.write('otro texto')

#archivo.close()

ruta = str(pathlib.Path().absolute()) + '/fichero_texto.txt'
archivo_lectura = open(ruta, 'r')

#Leer contenido y guardarlo
#contenido = archivo_lectura.read()

#Leer contenido y guardarlo en una lista

lista = archivo_lectura.readlines()
for fraces in lista:
    print(f' - {fraces}')

archivo_lectura.close()

ruta_original = str(pathlib.Path().absolute()) + '/fichero_texto.txt'
ruta_nueva =  str(pathlib.Path().absolute()) + '/ficheroNuevo_texto.txt'

#para copiar archivos
#shutil.copyfile(ruta_original, ruta_nueva)

#Pra morver archivos
# shutil.move(ruta_original,ruta_nueva)


os.remove(ruta_nueva)