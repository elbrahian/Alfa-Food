import os
from models.usuarios import *

from models.restaurantes import *
from models.productos import *

usuario = Usuarios()
restaurante = Restaurantes()
productos=Productos()


def MenuAdmin(connection, user):
    global restaurante

    while True:
        print(
            f"""
            ========={user[7]}==========
            ============================
            =======MENU PRINCIPAL=======

                * Opcion 1: USUARIOS 
                * Opcion 2: RESTAURANTE
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
                    1: 'ADMIN',
                    2: 'COCINERO',
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

                usuario.CrearUsuario(connection, documento, nombre, rol, True, telefono, contrasena,user[6])
                print("Usuario creado correctamente.")

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
                    usuarios = usuario.ObtenerUsuariosPorRestaurante(connection,user[6])
                    for i, usuario_info in enumerate(usuarios, start=1):
                        if (not(usuario_info[4])):
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
                    usuarios = usuario.ObtenerUsuariosPorRestaurante(connection,user[6])

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

            elif opcuser=='3':
                print("====LISTAR USUARIOS====")
                users = usuario.ObtenerUsuariosPorRestaurante(connection, user[6])
                if users:
                    for user_info in users:
                        print("ID:", user_info[0])
                        print("Documento:", user_info[1])
                        print("Nombre:", user_info[2])
                        print("Rol:", user_info[3])
                        print("Teléfono:", user_info[5])
                        print(f"Estado: {'Activo✅' if user_info[4] else 'Inactivo❌'}")
                        print("------------------------------")
                else:
                    print("No se encontraron usuarios para el restaurante con ID:", user[6])

            elif opcuser == '4':
                print("Regresando al menu principal")
            else:
                print("opcion invalida")

        elif opcion == "2":
            print(
                f"""
                =============MI RESTAURANTE:{user[7]}=============
                ** Opcion 1: Mis productos
                ** Opcion 2: Crear Productos
                ** Opcion 3: Volver al menu principal
                ======================================

                """
            )
            opcrestaurante = input("Seleccione que desea hacer: ")
            if opcrestaurante == '1':
                print("===========PRODUCTOS===========")
                pro=productos.ListarProductosPorRestaurante(connection,user[6])
                if pro:
                    for pro_info in pro:
                        print("ID:", pro_info[0])
                        print("Nombre:", pro_info[1])
                        print("Precio: $", pro_info[3])
                        print(f"Estado: {'Activo✅' if pro_info[2] else 'Inactivo❌'}")
                        print("------------------------------")
                else:
                    print("No se encontraron usuarios para el restaurante con ID:", user[6])

            elif opcrestaurante == '2':
                print("======CREAR PRODUCTO=====")
                nombre=input("Ingrese el Nombre del Producto: ")
                precio=float(input("Ingrese el Precio: "))
                new_pro=productos.CrearProductos(connection,nombre,precio,user[0])
                if(new_pro):
                    print(f"Producto: {nombre} ${precio} Creado")
                else:
                    print("Error al crear producto")
            elif opcrestaurante == '3':
                print("====LISTADO RESTAURANTES====")
                r = restaurante.ListarTodosLosRestaurantes(connection)
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