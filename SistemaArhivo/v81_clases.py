

#Trabajando con las clases

class Coche: # se recomienda que el nombre de clase empieze en mayuscula

    # Estos son las propiedad o atributos de una clase (Variables)
    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500

    #Metodos  o funciones, son las acciones que puede hacer objeto (Coche)

    def acelerar(self): #self debe ser puesta compa parametros para poder tener acceso a los atributos
        self.velocidad +=1

    def frenar(self):
        self.velocidad -=1

    def getvelocidad(self):
        return self.velocidad
    
    # OTRA FORMA ES UTILIZANDO LAS FUNCIONES SET Y GET ES MAS UN ESTANDAR

    def setcolor(self, color):
        self.color = color
    
    def getcolor(self):
        return self.color
    
    def setmodelo(self, modelo):
        self.modelo = modelo

    def getmodelo(self):
        return self.modelo
    

        
    
# De esta forma se crea un objeto (estancia de la clase)
coche = Coche()

""""
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
"""

coche.setcolor('azul')
coche.setmodelo('Toyota corla')


print( coche.getmodelo() , coche.getcolor())

print("-----------------------------------------------------------")

#Crear otro objeito con la misma clase coche

coche2 = Coche()

coche2.setmodelo('Honda Civic')
coche2.setcolor('Rojo')

print(coche2.getcolor(), coche2.getmodelo())