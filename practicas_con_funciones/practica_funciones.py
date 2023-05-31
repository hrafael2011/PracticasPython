"""
Función que devuelve la cantidad de caracteres en una cadena:
La función debe recibir una cadena de texto como parámetro.
La función debe devolver un número que representa la cantidad de caracteres en la cadena.

"""

def CantidadCaracteres(caracteres):

    C_caracters = len(caracteres)

    return C_caracters

cantid_caracter = CantidadCaracteres('Esto son las cantidades de caracteres')
print(f'La cantantidad de caracteres es: {cantid_caracter}')