
texto = 'Hendrick Rafael'

comprobar = isinstance(texto, str)

if comprobar:
    print('es un string')
else:
    print('no es un string')

if not isinstance(texto, float):
    print('no es un float')
else:
    print('es otro tipo de dato')

texto2 = "   texto con espacio   "
nombre = 'Hendrick'

print(texto2.strip()) #quita los espacios
print(nombre.lower()) #convierte el texto en miniscula
print(nombre.upper()) #convierte el texto en mayuscula
print(nombre.capitalize())
print(len(nombre)) #cuenta la cantidad de caracteres
print(texto2.find('t')) #busca una palabra o letra y la sustituye
print(texto2.replace('texto', 'palabra').strip())# reemplaza una palabra