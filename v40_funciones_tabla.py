
# Tabla funciones

def tabla(numero):
    print(f'***************** La tabla de multiplicar del {numero}************')
    for contador in range(11):
        operacion = contador * numero
        print(f'{numero} x {contador} = {operacion}')
    print('\n')
tabla(1)
tabla(2)

print('-----------------------------------------------------------')

for num_tabla in range(1,11):
    tabla(num_tabla)