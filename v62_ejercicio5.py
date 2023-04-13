
tabla = [

    {
        'Categoria': 'Accion',
        'Juego': ['Street Fighter','Medal of Honor', 'Call of duty']
    },

    {
        'Categoria': 'Aventura',
        'Juego': ['Mario Bros', 'Legend of zelda', 'Final Fantasy']
    },

    {
        'Categoria': 'Deportes',
        'Juego': ['NBA 2k22','MVP', 'Fifa']
    }

]


for caregori in tabla:
    print(f"----------------{caregori['Categoria']}---------------")
    for juego in caregori['Juego']:
        print(juego)
