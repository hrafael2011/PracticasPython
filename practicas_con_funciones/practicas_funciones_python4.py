"""
Función que calcula el área de un círculo:
La función debe recibir un parámetro numérico que representa el radio del círculo.
La función debe devolver un número que representa el área del círculo.

"""
pi = 3.14

def AreaCirculo(unidades):

    area = pi * (unidades^2)
    return area

print(AreaCirculo(6))
print(AreaCirculo(7))
