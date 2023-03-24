
def getEployee(nombre, cedula = False):
    print('*****informacion del empleado *****')
    print('\n')

    print(f'El nombre del empleado es {nombre}')
    if cedula != False:
        print(f'La cedula de epleado es {cedula}')

    

getEployee('hendrick', 22230098)