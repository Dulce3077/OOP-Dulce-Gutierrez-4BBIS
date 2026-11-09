import psycopg2
from psycopg2.extras import RealDictCursor
from .config import DB_config

class Database_connection:
    def __init__(self):
        self.config = DB_config

    def obtener_conexion(self):
        try:
            conexion = psycopg2.connect(**self.config)
            return conexion
        except Exception as e:
            print(f"Error al conectar con PostgreSQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.obtener_conexion()
        if not conexion:
            return None

        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()

    
    def ejecutar_comando(self, query, params=()):
        conexion = self.obtener_conexion()

        if not conexion:
            return False

        cursor = conexion.cursor()

        try:
            cursor.execute(query, params)
            conexion.commit()
            return True

        except Exception as e:
            print(f"Error al ejecutar el comando SQL: {e}")
            conexion.rollback()
            return False

        finally:
            cursor.close()
            conexion.close()
