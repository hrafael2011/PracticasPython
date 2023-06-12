
from clases import persona


class Informatico(persona):
    def __init__(self):
        self.lenguajes = 'html, css, python, javascritp'
        self.experecia = '5 anios'

    
    def set_lenguajes(self,lenguajes):
        self.lenguajes = lenguajes

    def set_experiencia(self,expereicia):
        self.experecia = expereicia

    def get_lenguajes(self):
        return self.lenguajes
    
    def get_experiencia(self):
        return self.experecia
        
