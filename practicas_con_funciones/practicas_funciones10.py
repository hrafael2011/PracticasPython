

matriz = [
        [1,2,3,4,5],
        [10,20,30,50,40]
    ]

def BuscarMatriz(lista):

    num_mayor = int()
    for fila in matriz:
        for elemento in fila:
            if elemento > num_mayor:
                num_mayor = elemento

    print(F'el numero mayor es {num_mayor}')
    

BuscarMatriz(matriz)