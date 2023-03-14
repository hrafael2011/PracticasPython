
#or y negacion

pais = 'Rusia'

if pais == 'colombia' or pais =='espana':
    print(f'{pais}, es de habla hispana')
else:
    print('no es de habla hispana')

if not(pais == 'colombia' or pais =='espana'):
    print('no son paises de habla hispana')
else:
    print(f'{pais}, es  de habla hispana')
    
if pais != 'colombia' or pais !='espana':
    print(f'{pais}, no es de habla hispana')
else:
    print(' es de habla hispana')
