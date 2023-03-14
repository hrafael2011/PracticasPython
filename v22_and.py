

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input('Introduce tu edad: '))


if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print('puede trabajar')
else:
    print('no puede trabajar')