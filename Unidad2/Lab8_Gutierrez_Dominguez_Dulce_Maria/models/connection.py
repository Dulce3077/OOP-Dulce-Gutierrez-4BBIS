import psycopg2 

class Conexion:
    def __init__(self):
        self.host = "localhost"
        self.usuario = "postgres"  
        self.password = "Dm061001"  
        self.base_datos = "login_mvc"
        self.port = "5432"

    def conectar(self):
        try:
            conexion = psycopg2.connect(
                host=self.host,
                user=self.usuario,
                password=self.password,
                database=self.base_datos,
                port=self.port
            )
            return conexion
        except psycopg2.Error as error:
            print("Error al conectar con PostgreSQL:", error)
            return None