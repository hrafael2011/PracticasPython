
def Recorrer_lista_8Num():

    num =[1,2,3,4,5,7,9, 10]

    print('***********mostrar*************')
    for nu in num:
        print(nu)

    print('***********Ordernar*************')
    num.sort()
    for nume in num:
        print(nume)

    print('************Mostrar longitud*********')
    print(len(num))

    buscar = int(input('Diga el numero: '))
    print(buscar in num)
    
Recorrer_lista_8Num()



