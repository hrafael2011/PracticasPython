#elif


dia = int(input('intruduzca en numero el dia de la semana que desea: '))

if dia == 1:
    print('lunes')
elif dia == 2:
    print('martes')
elif dia == 3:
    print('Miercoles')
elif dia == 4:
    print('Jueves')
elif dia == 5:
    print('Viernes')
elif dia == 6 or dia ==7:
    print('es fin desemana')
elif dia != 1 and dia !=7:
    print('no es un dia de semana')

