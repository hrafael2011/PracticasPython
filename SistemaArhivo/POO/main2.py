

from Practica_clase import persona


persona1 = persona('Hendrick', 'Rafael', 33, '178')


variable = ""
variable += '\n'
variable +=f'Nombre: {persona1.getNombre()}' 
variable += '\n'
variable += f'Apellido: {persona1.getApellido()}'
variable += '\n'
variable += f'Edad: {persona1.getEdad()}'
variable += '\n'
variable += f'Estatura: {persona1.getEstatura()}'

print(variable)