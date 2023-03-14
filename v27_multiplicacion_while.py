#multiplicacion con while


insertar_numero = int(input('inserte un numero: '))

if insertar_numero < 1:
    insertar_numero = 1


contador = 0

while contador <=9:
    contador = contador + 1
    print(f'{insertar_numero} x {contador} = {insertar_numero*contador}')
