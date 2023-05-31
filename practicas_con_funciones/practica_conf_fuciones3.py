"""
Función que convierte una cadena a una lista de caracteres:
La función debe recibir una cadena de texto como parámetro.
La función debe devolver una lista de caracteres que representan cada uno de los caracteres de la cadena original.


"""

def listaCaracteres(lista):
    numeroCarecteres = len(lista)
    contador = 0
    for num in lista:
        contador = contador + 1
        print(f'{contador}. {num}')

listaCaracteres('esto es un caracter')

