
calificacio = 0
aprobado = 0
reprobado=0
contador = 0
while contador <=15:
    contador = contador + 1
    calificacio = int(input('inserte calificacion: '))
    
    if calificacio >=70:
        aprobado = aprobado+1
    else:
        reprobado =reprobado+1
    if contador == 15:
        print(f'la cantidad de aprobados fue de {aprobado}')
        print('\n')
        print(f'la cantidad de reprobados fue de {reprobado}')

