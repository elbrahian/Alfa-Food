import psycopg2

class Mesas():
    id= ""
    estado= True

    def __init__(self):
        pass

    def CrearMesa(self, conexion, estado):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO mesas(estado) VALUES (%s);"
                cursor.execute(consulta, (estado,))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def DesactivarMesas(self, conexion, id_mesa):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE mesas SET estado = False WHERE id = %s;"
                cursor.execute(consulta, (id_mesa,))
                conexion.commit()
                return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def ActivarMesas(self, conexion, id_mesa):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE mesas SET estado = True WHERE id = %s;"
                cursor.execute(consulta, (id_mesa,))
                conexion.commit()
                return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def ListarMesasActivas(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta ="""SELECT * FROM mesas WHERE estado = true;"""
                cursor.execute(consulta)
                mesas_activas = cursor.fetchall()
                return mesas_activas
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ListarMesas(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta ="""SELECT id,estado FROM mesas;"""
                cursor.execute(consulta)
                mesas_activas = cursor.fetchall()
                return mesas_activas
        except psycopg2.Error as e:
            print("ERROR", e)
            return None




