
peliculas = ['el senor de los anillos','Thor', 'the man stil']

nueva_peli = ''
while nueva_peli != 'para':
    nueva_peli = input('introduzca una peli: ')

    if nueva_peli != 'para':
        peliculas.append(nueva_peli)


for pelicula in peliculas:
    print(f'{peliculas.index(pelicula)+1}. {pelicula}')