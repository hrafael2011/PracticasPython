"""
    --Proyecto phyton y MySql--
        -Abrir Asistente.
        -Login o Registro.
        -Si elegimos registro, creara un usuario en la base de datos.
        -Si Elegimos Login, identificara al usuario y nos preguntara.
        -Crear notas, mostrar notas, borrarlas.

    

"""
import acciones
print(
    """
    Acciones Disponible:
        1.Registro
        2.Login
    """
)

hazel = acciones.Acciones()
accion = int(input("Que quieres hacer:"))

if accion == 1:
    hazel.registro()
elif accion == 2:
    hazel.login()