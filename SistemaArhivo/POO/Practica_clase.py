
class persona:
    def __init__(self, nombre, apellido, edad, estatura):
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def setEdad(self, edad):
        self.edad = edad

    def setEstatura(self, estatura):
        self.estatura = estatura

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getEdad(self):
        return self.edad
    
    def getEstatura(self):
        return self.estatura
    
    