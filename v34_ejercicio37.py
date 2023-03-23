# rango numeros impares

numero1 = int(input('inserte el primer numero: '))
numero2 = int(input('inserte el segundo numero: '))

for num in range(numero1,numero2+1):
   if numero1 < numero2:
    if num%2  != 0:
        print(f'{num} impar')
    else:
       print(f'{num} par')
else:
   print('no es menor que el primer numero')



