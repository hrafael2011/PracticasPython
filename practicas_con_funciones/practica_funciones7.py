"""
Función que calcula la suma de los números pares de una lista:
La función debe recibir una lista de números como parámetro.
La función debe devolver la suma de los números pares de la lista.

"""

def NumerosPares(listaPares):

    par = []
    for num in listaPares:
        if num % 2 == 0:
            par.append(num)
            
        
    return par      
      
pares = NumerosPares([1,2,3,4,5,6,7,8])
print(sum(pares))