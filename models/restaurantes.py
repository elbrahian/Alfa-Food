import psycopg2
from models.usuarios import *

usuario = Usuarios()
class Restaurantes():
    id=""
    nombre=""
    estado=True
    img=""

    def __init__(self):
        pass

    def CrearRestaurante(self, conexion,nombre,id_user):
        try:
            u=usuario.ObtenerUsuarioPorID(conexion,id_user)
            if u[3]=="SUPERADMIN" and u[4]:
                with conexion.cursor() as cursor:
                    consulta_existencia = "SELECT nombre FROM restaurantes WHERE nombre = %s;"
                    cursor.execute(consulta_existencia, (nombre,))
                    usuario_existente = cursor.fetchone()
                    if usuario_existente:
                        print("Ya existe un restaurante")
                        return False

                with conexion.cursor() as cursor:
                    consulta = """INSERT INTO restaurantes(nombre,estado,"createdAt", "updatedAt") VALUES (%s,%s, NOW(), NOW());"""
                    cursor.execute(consulta, (nombre,True))
                conexion.commit()
                return True
            else:
                print("Unauthorized")
        except psycopg2.Error as e:
            print("ERROR", e)
            return False



    def ActivarRestaurante(self, conexion, restaurante_id, id_user):
        try:
            u = usuario.ObtenerUsuarioPorID(conexion, id_user)
            if u[3] == "SUPERADMIN" and u[4]:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE restaurantes SET estado = %s WHERE id = %s;"
                    cursor.execute(consulta, (True, restaurante_id))
                conexion.commit()
                return True
            else:
                print("Unauthorized")
                return False
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def DesactivarRestaurante(self, conexion, restaurante_id, id_user):
        try:
            u = usuario.ObtenerUsuarioPorID(conexion, id_user)
            if u[3] == "SUPERADMIN" and u[4]:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE restaurantes SET estado = %s WHERE id = %s;"
                    cursor.execute(consulta, (False, restaurante_id))
                conexion.commit()
                return True
            else:
                print("Unauthorized")
                return False
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def ListarRestaurantePorID(self, conexion, restaurante_id):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT id, nombre, estado, img FROM restaurantes WHERE id = %s;"
                cursor.execute(consulta, (restaurante_id,))
                restaurante = cursor.fetchone()
                if restaurante:
                    return restaurante
                else:
                    print("Restaurante no encontrado")
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ListarRestaurantePorNombre(self, conexion, nombre):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT id, nombre, estado, img FROM restaurantes WHERE nombre = %s;"
                cursor.execute(consulta, (nombre,))
                restaurante = cursor.fetchone()
                if restaurante:
                    return restaurante
                else:
                    print("Restaurante no encontrado")
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ListarTodosLosRestaurantes(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT id, nombre, estado, img FROM restaurantes;"
                cursor.execute(consulta)
                restaurantes = cursor.fetchall()
                if restaurantes:
                    return restaurantes
                else:
                    print("No se encontraron restaurantes en la base de datos")
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None



