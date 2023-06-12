
from informatico import Informatico
#import informatico

info = Informatico()



info.set_nombre("Hendrick")
info.set_apellido("Rafael")
info.set_edad('33')
info.accion_caminar()


cadena = "----------Info-----------"
cadena += " \n Nombre: "+ info.get_nombre()
cadena += " \n Apellido: "+ info.get_apellido()
cadena += " \n Edad: "+ info.get_edad()
cadena += " \n"+ info.accion_caminar()
cadena += " \n tengo conocimiento en los siguientes lenguajes: "+ info.get_lenguajes()
cadena += " \n Tengo"+ " "+info.get_experiencia() +" de experiencia"

print(cadena)






