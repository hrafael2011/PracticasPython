import usuario as md


class Acciones:
    
    def registro(self):

        print('n\Ok. Vamos a registrarte el sistema')

        nombre = input("Cual es tu nombre: ")
        apellido = input("Cuales son tus apellidos: ")
        email = input("cual es tu email: ")
        passw = input("cual es tu contrasena: ")

        user = md.Usuario(nombre, apellido, email, passw)
        
        registro = user.registrar()

        if registro[0]>=1:
            print(f'Registro completado {registro[1].nombre}')

        else:
            print('\n','no se regisgro con exito')

    def login(self):

        print("n\Identificate en el sistema")

        try:
            email = input("cual es tu email: ")
            passw = input("cual es tu contrasena: ")

            usuario = md.Usuario('','', email, passw)
            login = usuario.identificar()

            if email == login[3]:
                print(f'Bienvenido {login[1]} has iniciado seccion con el emial {login[3]}')
                self.proximaAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'Login incorrecto')

    def proximaAcciones(self, usuario):
        print("""

            Acciones Disponible:

                1. Crear notas
                2. Mostrar tus notas
                3. Eliminar Notas
                4. Salir
          """)
        

        acciones = int(input('Que quieres hacer?'))

        if acciones == 1:
            print('crear notas')
            self.proximaAcciones(usuario)
        elif acciones == 2:
            print('mostrar notas')
            self.proximaAcciones(usuario)
        elif acciones == 3:
            print('Eliminar nota')
            self.proximaAcciones(usuario)
        elif acciones == 4:
            print('\n')
            print(f'ok, Hasta pronto {usuario[2]}')
            exit()




        


        
    