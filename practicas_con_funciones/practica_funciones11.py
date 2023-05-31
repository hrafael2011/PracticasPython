"""
Función que calcula el promedio de una lista de números, excluyendo el valor más alto y el valor más bajo:
La función debe recibir una lista de números como parámetro.
La función debe devolver el promedio de la lista, excluyendo el valor más alto y el valor más bajo.

"""

lista = [90,85,100,90]
def PromedioLista(promedio):

    lista.pop()
    del lista[0]
    resultado = sum(lista)/len(lista)
    
    return resultado

print(PromedioLista(lista))