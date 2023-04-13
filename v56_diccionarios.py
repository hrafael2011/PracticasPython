
#Diccionarios

personas = [
{
    
    'nombre': 'Hendrick',
    'Apellido': 'Rafael',
    'Email': 'inghendrickRafael@gmail.com'
},
{
    'nombre': 'Alexander',
    'Apellido': 'Acosta',
    'Email': 'alexander@gmail.com'

}
]

#print(personas['Apellido'])


for persona in personas:
    print(f'El nombre es {persona["nombre"]}')
    print(f'El correo es {persona["Email"]}')
    print('\n')