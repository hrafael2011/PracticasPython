class casa:

    def setCosina(self, cosina):
        self.cosina = cosina
    
    def setHabitaciones(self, habitaciones):
        self.habitaciones = habitaciones

    def setSala(self, sala):
        self.sala = sala

    def setMarquesina(self, marquesina):
        self.marquesina = marquesina

    def setBanos(self, banos):
        self.banos = banos

    def getCosinas(self):
        return self.cosina
    
    def getHabitaciones(self):
        return self.habitaciones
    
    def getSalas(self):
        return self.sala
    
    def getMarquesina(self):
        return self.marquesina
    
    def getBanos(self):
        return self.banos
    
class apartamento(casa):

    def setAarqueos(self, parqueos):
        self.paqueos = parqueos
    
    def getParuqeos(self):
        return self.paqueos
        
        