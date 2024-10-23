import psycopg2
import uuid
from models.usuarios import *
usuario=Usuarios()
class Productos():
    id=""
    documento=""
    nombre=""
    rol=""
    estado=True
    telefono=""
    password=""
    restaurante=0

    def __init__(self):
        pass

    def CrearProductos(self, conexion, nombre,precio,id_user):
        try:
            u=usuario.ObtenerUsuarioPorID(conexion,id_user)
            if u[4]:
                with conexion.cursor() as cursor:
                    consulta = """
                        INSERT INTO productos(id, nombre, estado, precio, restaurante, "createdAt", "updatedAt")
                        VALUES (%s, %s, %s, %s, %s,NOW(), NOW());
                    """
                    cursor.execute(consulta, (str(uuid.uuid4()),nombre, True, precio,u[6]))
                conexion.commit()
                return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def ListarProductosPorRestaurante(self, conexion, id_restaurante):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id, nombre, estado, precio
                    FROM productos
                    WHERE restaurante = %s;
                """
                cursor.execute(consulta, (id_restaurante,))
                resultados = cursor.fetchall()
                if resultados:
                    return resultados
                else:
                    print("No se encontraron productos para el restaurante con ID:", id_restaurante)
                    return []
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ListarProductos(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id, nombre, estado, precio FROM productos """
                cursor.execute(consulta)
                resultados = cursor.fetchall()
                if resultados:
                    return resultados
                else:
                    print("No se encontraron productos")
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ActivarProducto(self, conexion, producto_id,id_user):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    UPDATE productos
                    SET estado = True
                    WHERE id = %s;
                """
                cursor.execute(consulta, (producto_id,))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def DesactivarProducto(self, conexion, producto_id,id_user):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    UPDATE productos
                    SET estado = False
                    WHERE id = %s;
                """
                cursor.execute(consulta, (producto_id,))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def ObtenerProductoPorID(self, conexion, producto_id):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id, nombre, estado, precio, restaurante
                    FROM productos
                    WHERE id = %s;
                """
                cursor.execute(consulta, (producto_id,))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado
                else:
                    print("Producto no encontrado.")
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return

    def ObtenerProductoPorIDRestaurante(self, conexion, producto_id, restaurante_id):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id, nombre, estado, precio, restaurante
                    FROM productos
                    WHERE id = %s AND restaurante = %s;
                """
                cursor.execute(consulta, (producto_id, restaurante_id))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado
                else:
                    print("Producto no encontrado.")
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None





