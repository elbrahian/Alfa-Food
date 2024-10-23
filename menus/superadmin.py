import os
from models.usuarios import *

from models.restaurantes import *

usuario = Usuarios()
restaurante = Restaurantes()

def MenuSuperAdmin(connection, user):

    global restaurante

    while True:
        print(
            """
            =========FOOD ALFA==========
            ============================
            =======MENU PRINCIPAL=======

                * Opcion 1: USUARIOS 
                * Opcion 2: RESTAURANTES
                * Opcion 3: SALIR

            ============================
            ============================
            """
        )
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            os.system('cls')
            print(
                """
                ==============USUARIOS==================

                    * Opcion 1: Crear usuario
                    * Opcion 2: Cambiar estado
                    * Opcion 3: Listar Usuarios
                    * Opcion 4: Volver al menu principal

                ========================================

                """
            )
            opcuser = input("Seleccione una opcion: ")

            if opcuser == '1':
                print(
                    """
                    ====CREAR USUARIO====
                    """
                )
                documento = input("Digite el numero de documento: ")

                nombre = input("Digite el nombre: ")

                roles = {
                    1: 'SUPERADMIN',
                    2: 'ADMIN',
                    3: 'MESERO',
                    4: 'COCINERO',
                }
                print("Seleccione su rol: ")
                for i, rol in roles.items():
                    print(f'{i} - {rol}')
                opcrol = int(input('Ingrese su opción: '))
                rol = roles.get(opcrol)
                if rol is None:
                    rol = None

                telefono = int(input("Ingrese el telefono: "))
                contrasena = input("Ingrese una contraseña: ")
                if rol=="SUPERADMIN":
                    usuario.CrearUsuario(connection, documento, nombre, rol, True, telefono, contrasena,0)
                else:
                    r = restaurante.ListarTodosLosRestaurantes(connection)
                    restaurant = {}
                    for i, restaurante_info in enumerate(r):
                        restaurant[restaurante_info[0]] = restaurante_info[1]

                    for i, restaurante_nombre in restaurant.items():
                        print(f'{i} - {restaurante_nombre}')

                    opcrest = int(input("Ingrese el número correspondiente al restaurante al que pertenece: "))
                    print(opcrest)
                    restaurante_elegido = opcrest
                    if restaurante_elegido is not None:
                        usuario.CrearUsuario(connection, documento, nombre, rol, True, telefono, contrasena,
                                             restaurante_elegido)
                        print("Usuario creado correctamente.")
                    else:
                        print("Número de restaurante inválido. No se creará el usuario.")

            elif opcuser == '2':
                print(
                    """
                  =======CAMBIAR ESTADO=======
                  
                    * Opcion 1: Activar
                    * Opcion 2: Desactivar
                    * Opcion 3: Volver al menu
                  ============================

                    """
                )
                opcestadouser = input("Seleccione una opcion: ")

                if opcestadouser == '1':
                    print("====ACTIVAR====")
                    usuarios = usuario.ObtenerUsuarios(connection)

                    for i, usuario_info in enumerate(usuarios, start=1):
                        if(not(usuario_info[4])):
                            print(f"{i}. Nombre: {usuario_info[2]}")

                    seleccion = int(input("Ingrese el número del usuario a activar: "))
                    if 1 <= seleccion <= len(usuarios):
                        id_usuario = usuarios[seleccion - 1][0]
                        if usuario.ActivarUsuario(connection, id_usuario):
                            print("Usuario activado")
                        else:
                            print("Error al activar usuario")
                    else:
                        print("Número de usuario no válido")


                elif opcestadouser == '2':
                    print("====DESACTIVAR====")
                    usuarios = usuario.ObtenerUsuarios(connection)

                    for i, usuario_info in enumerate(usuarios, start=1):
                        if (usuario_info[4]):
                            print(f"{i}. Nombre: {usuario_info[2]}")

                    seleccion = int(input("Ingrese el número del usuario a desactivar: "))
                    if 1 <= seleccion <= len(usuarios):
                        id_usuario = usuarios[seleccion - 1][0]
                        if usuario.DesactivarUsuario(connection, id_usuario):
                            print("Usuario Desactivado")
                        else:
                            print("Error al desactivar usuario")
                    else:
                        print("Número de usuario no válido")

                elif opcestadouser == '3':
                    print("Regresando...")

                else:
                    print("Opcion invalida")

            elif opcuser == '3':
                print("====LISTAR USUARIOS====")
                users = usuario.ObtenerUsuarios(connection)
                if users:
                    for user_info in users:
                        print("ID:", user_info[0])
                        print("Documento:", user_info[1])
                        print("Nombre:", user_info[2])
                        print("Rol:", user_info[3])
                        print("Teléfono:", user_info[5])
                        print(f"Estado: {'Activo✅' if user_info[4] else 'Inactivo❌'}")
                        print("Nombre del Restaurante:", user_info[7])
                        print("------------------------------")
                else:
                    print("No se encontraron Usuarios")

            elif opcuser == '4':
                print("Regresando al menu principal")
            else:
                print("opcion invalida")

        elif opcion == "2":
            print(
                """
                =============RESTAURANTES=============
                
                ** Opcion 1: Crear restaurante
                ** Opcion 2: Cambiar estado
                ** Opcion 3: Listar restaurantes
                ** Opcion 4: Volver al menu principal
                ======================================

                """
            )
            opcrestaurante = input("Seleccione que desea hacer: ")
            if opcrestaurante == '1':
                print("====Crear Restaurante====")
                nombre = input("Nombre del Restaurante: ")
                new_r=restaurante.CrearRestaurante(connection,nombre,user[0])
                if(new_r):
                    print(f"Restaurante: {nombre}, creado con exito")

            elif opcrestaurante == '2':
                print(
                    """
                    ======CAMBIAR ESTADO======
                    
                    * Opcion 1: Activar
                    * Opcion 2: Desactivar
                    * Opcion 3: Volver al menu
                    ==========================

                    """
                )
                opcestadorest = input("Seleccione que desea hacer: ")

                if opcestadorest == '1':
                    print("====ACTIVAR====")
                    restaurantes = restaurante.ListarTodosLosRestaurantes(connection)

                    for i, restaurante_info in enumerate(restaurantes, start=1):
                        if (not (restaurante_info[2])):
                            print(f"{i}. Nombre: {restaurante_info[1]}")

                    seleccion = int(input("Ingrese el número del restaurante a activar: "))
                    if 1 <= seleccion <= len(restaurantes):
                        id_restaurante = restaurantes[seleccion - 1][0]
                        if restaurante.ActivarRestaurante(connection, id_restaurante,user[0]):
                            print("Restaurante activado")
                        else:
                            print("Error al activar usuario")
                    else:
                        print("Número de restaurante no válido")

                elif opcestadorest == '2':
                    print("====DESACTIVAR====")
                    restaurantes = restaurante.ListarTodosLosRestaurantes(connection)

                    for i, restaurante_info in enumerate(restaurantes, start=1):
                        if (restaurante_info[2]):
                            print(f"{i}. Nombre: {restaurante_info[1]}")

                    seleccion = int(input("Ingrese el número del restaurante a activar: "))
                    if 1 <= seleccion <= len(restaurantes):
                        id_restaurante = restaurantes[seleccion - 1][0]
                        if restaurante.DesactivarRestaurante(connection, id_restaurante, user[0]):
                            print("Restaurante activado")
                        else:
                            print("Error al activar usuario")
                    else:
                        print("Número de restauranet no válido")

                elif opcrestaurante == '3':
                    print("Regresando...")

                else:
                    print("Opcion incorrecta")

            elif opcrestaurante == '3':
                print("====LISTADO RESTAURANTES====")
                r=restaurante.ListarTodosLosRestaurantes(connection)
                if r:
                    print("Lista de Restaurantes:")
                    for restaurante_info in r:
                        print(f"ID: {restaurante_info[0]}")
                        print(f"Nombre: {restaurante_info[1]}")
                        print(f"Estado: {'Activo✅' if restaurante_info[2] else 'Inactivo❌'}")
                        print(f"Imagen: {restaurante_info[3]}")
                        print("=======================================================")
                else:
                    print("No se encontraron restaurantes en la base de datos.")


            elif opcrestaurante == '4':
                print("Regresando...")
            else:
                print("Opcion invalida")

        elif opcion == '3':
            print("Cerrando sesion...")
            print("Hasta luego")
            break
        else:
            print("Opción no válida")