import psycopg2
import bcrypt
import uuid
class Usuarios():
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

    def CrearUsuario(self, conexion, documento, nombre, rol, estado, telefono, password, restaurante):
        try:
            # Verificar si el usuario ya existe con el mismo documento
            with conexion.cursor() as cursor:
                consulta_existencia = "SELECT id FROM usuarios WHERE documento = %s;"
                cursor.execute(consulta_existencia, (documento,))
                usuario_existente = cursor.fetchone()
                if usuario_existente:
                    print("Ya existe un usuario")
                    return False

            if rol == "SUPERADMIN" or rol == "MESERO":
                restaurante = 0

            salt = bcrypt.gensalt(rounds=6)
            password = bcrypt.hashpw(password.encode('utf-8'), salt)

            with conexion.cursor() as cursor:
                consulta = """
                    INSERT INTO usuarios(id, documento, nombre, rol, estado, telefono, password, restaurante, "createdAt", "updatedAt")
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW());
                """
                cursor.execute(consulta, (str(uuid.uuid4()), documento, nombre, rol, estado, telefono, str(password.decode('utf-8')),restaurante))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def ObtenerUsuarios(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                           SELECT u.id, u.documento, u.nombre, u.rol, u.estado, u.telefono, r.id as id_restaurante, r.nombre as nombre_restaurante
                           FROM usuarios u
                           JOIN restaurantes r ON u.restaurante = r.id
                       """
                cursor.execute(consulta)
                usuarios_info = cursor.fetchall()
                return usuarios_info
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ObtenerUsuariosPorRestaurante(self, conexion, id_restaurante):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                           SELECT u.id, u.documento, u.nombre, u.rol, u.estado, u.telefono, r.id as id_restaurante, r.nombre as nombre_restaurante
                           FROM usuarios u
                           JOIN restaurantes r ON u.restaurante = r.id
                           WHERE r.id = %s
                       """
                cursor.execute(consulta, (id_restaurante,))
                usuarios_info = cursor.fetchall()
                return usuarios_info
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ObtenerUsuarioPorID(self, conexion, id_usuario):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                       SELECT u.id, u.documento, u.nombre, u.rol, u.estado, u.telefono, r.id as id_restaurante, r.nombre as nombre_restaurante,r.img as imagen_restaunrte
                       FROM usuarios u
                       JOIN restaurantes r ON u.restaurante = r.id
                       WHERE u.id = %s;
                   """
                cursor.execute(consulta, (id_usuario,))
                usuario_info = cursor.fetchone()
                return usuario_info
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def DesactivarUsuario(self, conexion, id_usuario):
        try:
            with conexion.cursor() as cursor:
                consulta = """UPDATE usuarios SET estado = False, "updatedAt" = NOW() WHERE id = %s;"""
                cursor.execute(consulta, (id_usuario,))
                conexion.commit()
                return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def ActivarUsuario(self, conexion, id_usuario):
        try:
            with conexion.cursor() as cursor:
                consulta = """UPDATE usuarios SET estado = True, "updatedAt" = NOW() WHERE id = %s;"""
                cursor.execute(consulta, (id_usuario,))
                conexion.commit()
                return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def EditarUsuario(self, conexion, id_usuario, nuevo_documento, nuevo_nombre, nuevo_rol, nuevo_telefono):
        try:
            with conexion.cursor() as cursor:
                consulta = """UPDATE usuarios SET nombre = %s, "updatedAt" = NOW() WHERE id = %s;"""
                parametros = (nuevo_nombre, id_usuario)

                if nuevo_documento is not None:
                    consulta += """UPDATE usuarios SET documento = %s, "updatedAt" = NOW() WHERE id = %s;"""
                    parametros += (nuevo_documento, id_usuario)

                if nuevo_rol is not None:
                    consulta += """UPDATE usuarios SET rol = %s, updatedAt = NOW() WHERE id = %s;"""
                    parametros += (nuevo_rol, id_usuario)

                if nuevo_telefono is not None:
                    consulta += """UPDATE usuarios SET telefono = %s, updatedAt = NOW() WHERE id = %s;"""
                    parametros += (nuevo_telefono, id_usuario)

                cursor.execute(consulta, parametros)
                conexion.commit()
                return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def Login(self, conexion, documento, password):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT u.id, u.documento, u.password, u.estado, r.id, r.nombre, r.estado " \
                           "FROM usuarios u " \
                           "LEFT JOIN restaurantes r ON u.restaurante = r.id " \
                           "WHERE u.documento = %s;"
                cursor.execute(consulta, (documento,))
                usuario = cursor.fetchone()

                if usuario and usuario[3] and usuario[6]:
                    stored_hash = usuario[2].encode('utf-8')
                    provided_password = password.encode('utf-8')
                    if bcrypt.checkpw(provided_password, stored_hash):
                        return usuario[0]
                    else:
                        return None
                else:
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None