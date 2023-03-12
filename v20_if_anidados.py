

#if anidados

nombre = "Hendrick Rafael"
continente = "Americano"
ciudad = "Santo Domingo"
edad = 33
mayoria_edad = 18

if edad >= mayoria_edad:
    if continente != "Americano":
        print(f'{nombre}, no eres americano')
    else:
        print(f'{nombre}, eres americano y eres de la ciudad de {ciudad}')
else:
    print(f'{nombre}, no eres yaor de edad')    