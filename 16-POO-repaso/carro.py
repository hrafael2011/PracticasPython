
class Carro:

    marca = "Honda"
    modelo = "Civic"
    tipo = "sedan"
    velocidad = 250

    def __init__(self, marca, modelo, tipo, velocidad):
        
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.velocidad = velocidad

    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca
    
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo
    
    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo
        
    def acelerar(self):
        self.velocidad +=1
    
    def frena(self):
        self.velocidad -=1

    def getInfo(self):

        info = "------Informacion--------"
        info += "\n Marca: "+ self.marca
        info += "\n Modelo: "+ self.modelo
        info += "\n tipo: "+ self.tipo
        info += "\n Velocidad: "+ str(self.velocidad)

        return info



"""

carro = Carro()



carro.set_marca("toyota")
carro.set_modelo("Vitz")

if carro.set_modelo('camry'):
    carro.set_tipo('sedan')
else:
    carro.set_tipo('otro tipo')

print(f'La marca es: {carro.get_marca()} y el modelo es: {carro.get_modelo()} el tipo de vehiculo es {carro.get_tipo()}')


print(f'velcidad actual {carro.velocidad}')
carro.acelerar()
carro.acelerar()
carro.acelerar()

print(f'velcidad aceleracion {carro.velocidad}')

carro.frena()

print(f'velcidad aceleracion {carro.velocidad}')


carro2 = Carro() # de esa manaera tenemos otro objeto

"""

 
