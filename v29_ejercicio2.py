
#numeros pares hasta el 120

""""
pares = 0

while pares <= 118:
    pares = pares + 2

    print(pares)
else:
    print("fin")

"""


contador = 0

for contador in range(1,121):
    if contador%2 == 0:
        print(contador)