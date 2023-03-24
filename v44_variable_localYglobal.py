
def HolaMundo():
    text = 'hola Mundo'
    #return text # retun hace que las variables puedan ser usada fuera de la funcion
    #global se utiliza para hacer que una variable se vuelva local , que pueda utilizar fuera de la funcion
    print('Dentro de la funcion: ', text)

print(HolaMundo())

text = 'hola Mundo'
print('Fuera de la funcion: ', text)