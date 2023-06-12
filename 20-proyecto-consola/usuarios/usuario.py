import datetime
import hashlib
import conexion as cn

conect = cn.conectar()
database = conect[0]
cursor = conect[1]


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    
    def registrar(self):

        #cifrado contrasena
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))# Es nesesario ponerle .encode('utf8') porque update viene en bite, y para que
                                                    #para que pueda ser reconocido como exageximal es nesesario hacerlo asi
        fecha = datetime.datetime.today()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)


        try:
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]


        return result

    
    def identificar(self):
        sql = "SELECT *FROM usuarios WHERE email=%s AND pass=%s"

        #cifrado contrasena
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)

        result = cursor.fetchone()

        return result 


        
        

        