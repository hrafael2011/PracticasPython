

class persona:

    """
    -nombre
    -apellido
    -sexo
    -edad

    """

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_sexot(self):
        return self.sexo
    
    def get_edad(self):
        return self.edad
    
    def accion_caminar(self):
        return 'estoy caminado'
    
    def accion_dormir(self):
        return 'Estoy durmiendo'
    
    def accion_comer(self):
        return 'Estoy comiendo'