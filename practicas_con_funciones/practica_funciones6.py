"""
Función que ordena una lista de números de menor a mayor:
La función debe recibir una lista de números como parámetro.
La función debe devolver una lista ordenada de menor a mayor.

"""

def ListaOrdernada(lista):
    lista.sort()
    lista.reverse()
    print(lista)
    
ListaOrdernada([1, 2, 4, 3, 6, 5])
