
from v84 import Coche2

carro = Coche2('Rojo','Honda', 'Civic', 300, 500)
carro1 = Coche2('Azul','Toyota', 'Corolla', 250, 500)
carro2 = Coche2('Verde','Honda', 'Civic', 150, 500)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())

#como identificar el tipo de mi objeto

if type(carro) == Coche2:
    print('Es correcto')
else:
    print('es incorrecto')