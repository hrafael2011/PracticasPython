import usuarios.conexion as concexion

conect = concexion.conectar()
database = conect[0]
cursor = conect[1]

class Notas:

    def __init__(self, usuario_Id, titulo, descripcion):
        self.usuario_Id = usuario_Id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):

        sql = "INSERT INTO notas VALUES(NULL, %s,%s,%s, NOW())"
        notas = (self.usuario_Id, self.titulo, self.descripcion)
        cursor.execute(sql,notas)
        database.commit()

        return[cursor.rowcount, self]

        