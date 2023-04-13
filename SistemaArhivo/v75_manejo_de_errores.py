

nombre = input("Escriba Su Nombre: ")

try:
    if len(nombre) > 1:
        nombre_usuario = 'El nombre es: ' + nombre
    print(nombre_usuario)
except:
    print('Hubo un error')
else:
    print('Todo Salio bien')
finally: 
    print('Fin de la interacion')

