
cantantes = ['Tego Carderon','Daddy Yanque', 'Lito', 'Polaco']
numeros = [1, 2, 4, 7, 9, 8]

#Orndenar
numeros.sort()
print(numeros)

#agregar
numeros.append(10)
print(numeros)
cantantes.insert(0,'Don Omar')
print(cantantes)

#eliminar
cantantes.pop(1)
numeros.remove(8)
print(cantantes)
print(numeros)

#Dar la vuelta
numeros.reverse()
print(numeros)

#Buscar en una lista
print('Lito' in cantantes)

#contar elementos de una lista
print(len(cantantes))

#cuantas veces aparece un elemento
numeros.append(9)
print(numeros.count(9))

#conseguir indice
print(cantantes.index('Polaco'))

#unir listas

cantantes.extend(numeros)
print(cantantes)