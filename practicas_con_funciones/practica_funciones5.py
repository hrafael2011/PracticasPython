"""

FFunción que verifica si dos listas tienen elementos comunes:
La función debe recibir dos listas como parámetros.
La función debe devolver True si las listas tienen al menos un elemento en común, y False si no tienen elementos en común.
"""

def CompararLista(lista1, lista2):

    if lista1[1] == lista2[1]:
        return True
    else:
        return False

print(CompararLista([4,23,45],[1,23,45]))



