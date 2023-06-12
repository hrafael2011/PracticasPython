import notas as modelo

class Acciones_notas:

    def crear(self, usuario):
        print(f'\n ok {usuario[1]}!!! vamos a crear una nueva nota')

        titulo = input('Introduce el titulo de l anota')
        descripcion = input('Introduce el contenido de la nota')

        nota = modelo.Notas(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\n se ha guardaro el titulo {nota.titulo} corretamente')
        else:
            print(f'\n No se ha guardado la nota los siento{usuario[1]}')


