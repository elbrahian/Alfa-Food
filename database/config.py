import psycopg2
class Basedatos():
    host = ""
    port = 7072
    user = ""
    password = ""
    database = ""

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        try:
            credenciales ={
                "dbname": self.database,
                "user": self.user,
                "password": self.password,
                "host": self.host,
                "port": self.port,
            }
            conexion = psycopg2.connect(**credenciales)
            if conexion:
                print("conexion exitosa")
            return conexion
        except psycopg2.Error as e:
            print("Error", e)