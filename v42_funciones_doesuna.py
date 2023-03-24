
def getName(nombre):
    texto = nombre
    return texto
def getAge(edad):
    texto = edad
    return texto

def getAll(nombre, edad):
    text = getName(nombre) + "\n" + str(getAge(edad))
    return text
print(getAll('Hendrick', 33))
