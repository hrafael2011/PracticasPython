import mysql.connector

#conexion

database = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd ="",
    database ="CursoPythonDB"

)

# para comprabarl aconexion
#print(database)

#CREAR BASE DE DATOS
cursor = database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS CursoPythonDB")
"""
#MOSTRAR LAS BASES DE DATOS EXISTENTES
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

"""
#crear tabla
cursor.execute(
"""
CREATE TABLE IF NOT EXISTS vehiculo(
vehiculo_ID INT primary key auto_increment not null,
marca varchar(100) not null,
modelo varchar(100) not null,
precio float(10,2) not null
)
"""

)
"""
cursor.execute("show tables")

for tb in cursor:
    print(tb)
"""
#INSERTAR 
#cursor.execute("INSERT INTO vehiculo VALUES(NULL,'HONDA','CRV',17000.00)")

#INSERTAR MULTIPLES DATOS
"""
coches=[
    ('Toyota','corolla',10000.00),
    ('Nissan','March',1000.00),
    ('Chevrolet','Aveo',12000.00)
]

cursor.executemany("INSERT INTO vehiculo values(null,%s,%s,%s)",coches)
database.commit()
"""
cursor.execute("Select *from vehiculo")
result = cursor.fetchall()
for coche in result:
    print(coche)
"""result = cursor.fetchall() #para mostrar todos
#result = cursor.fetchone() #para mostrar solo el primero
for coche in result:
    print(coche[1]) # para indicar el indice
"""


#eliminar 
"""
cursor.execute("DELETE FROM VEHICULO WHERE marca='toyota'")
database.commit()
"""
#actualizae
cursor.execute("UPDATE VEHICULO SET marca='Chevrloet' WHERE marca='Nissan'")
database.commit()