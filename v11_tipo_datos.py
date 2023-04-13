#tipos de datos python

#string

string = "esto es un string"
entero = 1
flotante = 1.5
booleano = False
lista = [4,5,6,7]
listaString = ["nombre", 25, "Apellido"]
tupla = ('mater','ingenieria', 'licenciatura')


print(type(string))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tupla))
print('\n')
print('----------------------------------------------')

for stri in range(5):
    print(str(stri) +'-'+string) 
    

for lis in lista:
    print(lis)
  

for lis2 in listaString:
    print(lis2)

for tu in tupla:
    print(tu)



#recorrer un array con while
contador = 0
n = len(lista)
while contador < n:
    print(lista[contador])
    contador+=1


    
