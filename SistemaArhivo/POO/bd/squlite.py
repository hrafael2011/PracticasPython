import sqlite3

#conexion
conexion = sqlite3.connect('pruebas.db')



#crear cursor , eso nos permita ejecurar las cosultas
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCT("+
"ID integer primary key autoincrement, "+
"titulo varchar(255), " +
"descripcion text, "+
"precio int(255)"              
               
")")

#guardar cambios
conexion.commit()


#insertar datos
"""
cursor.execute("INSERT INTO product VALUES(null, 'Maiz dulce','comestible','150')")
conexion.commit()
"""

#borrar datos
"""
cursor.execute("Delete from product")
conexion.commit()
"""

#insertar multiples datos

productos_varios = [

    ('Radio', 'electronico', '1200'),
    ('TV', 'electronico', '1200'),
    ('Lavadora', 'electronico', '1000'),
    ('Estufa', 'electronico', '500'),
    ('Aire', 'electronico', '20000')
]

"""
cursor.executemany("INSERT INTO product VALUES (null,?,?,?)",productos_varios)
conexion.commit()
"""

#Actualizar datos

cursor.execute("UPDATE PRODUCT SET PRECIO = 1500 WHERE PRECIO = 1200")
conexion.commit()

#listar producto
cursor.execute('SELECT *FROM product')
producto = cursor.fetchall()

#print(producto)

for pro in producto:
    print('Producto: ', pro[1])
    print('Tipo: ', pro[2])
    print('Precio: ', pro[3])
    print('\n')


#cerrar conexion
conexion.close()