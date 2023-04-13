
contactos = [
    [
    'Hendrick',
    'hendrick@gmail.com'
    ],
    [
    'Rafael',
    'rafael@gmail.com'
    ],
    [
    'Anthony',
    'anthony@gmail.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f'{contacto.index(elemento)+1}. Nombre: {elemento}')
        else:
            print(f'{contacto.index(elemento)+1}.Email: {elemento}')
    print('\n')

 
 