
""""
Función que verifica si una cadena es un pangrama:
La función debe recibir una cadena de texto como parámetro.
La función debe devolver True si la cadena es un pangrama (es decir, si contiene todas las letras del alfabeto al menos una

"""


def Pangrama(texto):

    palabra = texto.split()
    quitar_epacio = "".join(palabra)
    texto2= quitar_epacio

    unir = []
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']

    for tex in range(len(texto2)):
    
        #print(texto[tex].upper())
        unir.append(texto2[tex].upper())
    repitidos = list(set(unir)) # para eliminar elementos repetidos
    repitidos.sort()
    
    if repitidos == alfabeto:
        return True
    else:
        return False
    
  
texto3 = Pangrama("La ciguena llamada wander tocaba el saxofon detras del palenque de paja  uso el zapato corrio kilometros y el hilo ")
#texto3 = Pangrama("HOla Mundo")
print(texto3)


