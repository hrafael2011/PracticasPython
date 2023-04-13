
nombre = input('inserte nombre: ')
edad = int(input('inserte edad: '))
    
def tuNombreEdad(nombre, edad):
    print(f'Mi nombre es {nombre} y mi edad es {edad}')
    if edad >= 18:
        print('es mayor de edad')
    else:
        print('Es menor de edad')



tuNombreEdad(nombre, edad)
