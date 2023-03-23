

continuar = 'si'
while continuar == 'si':

    print('*********** Elija la opcion deseada******')
    print('1: suma')
    print('2: Resta')
    print('3: Multiplicacion')
    print('4: Division')

    opcion = int(input('seleccione la operacion deceada :'))

    if opcion == 1:
        valor1 = int(input('inserte el primer valor: '))
        valor2 = int(input('inserte el segundo valor: '))
        print(f'la suma de ambos numeros es {valor1 + valor2}')
    elif opcion == 2:
        valor1 = int(input('inserte el primer valor: '))
        valor2 = int(input('inserte el segundo valor: '))
        print(f'la resta de ambos numeros es {valor1 - valor2}')
    elif opcion == 3:
        valor1 = int(input('inserte el primer valor: '))
        valor2 = int(input('inserte el segundo valor: '))
        print(f'la multiplicacion de ambos numeros es {valor1 * valor2}')
    elif opcion == 4:
        valor1 = int(input('inserte el primer valor: '))
        valor2 = int(input('inserte el segundo valor: '))
        print(f'la divicion de ambos numeros es {valor1 / valor2}')
    else:
        print('Esa opcion no existe')
    
   

    continuar = input('decea continuar si/no: ')


    

    