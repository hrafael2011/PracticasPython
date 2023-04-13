class Coche2:

    def __init__(self, color, marca, modelo, velocidad, caballaje):

        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje

    def setcolor(self, color):
         self.color = color

    def getcolor(self):
        return self.color
        
    def setmarca(self, marca):
        self.marca = marca

    def getmarca(self):
         return self.marca
        
    def setmodelo(self, modelo):
         self.marca = modelo

    def getmodelo(self):
        return self.modelo

    def setvelocidad(self, velocidad):
         self.velocidad = velocidad

    def getvelocidad(self):
        return self.velocidad
        
    def setcaballaje(self, caballaje):
        self.caballaje = caballaje

    def getcaballaje(self):
        return self.caballaje
        

    def getInfo(self):

        info = '------INFO VEHICULOS----------'
        info += '\n' + ' Color: ' + self.getcolor()
        info += '\n' + 'Marca: '  + self.getmarca()
        info += '\n' + 'Modelo: ' + self.getmodelo()
        info += '\n' + 'velocidad: '+ str(self.getvelocidad())
        info += '\n' + 'Caballaje: ' + str(self.getcaballaje())

        return info

            
            
        
        

        