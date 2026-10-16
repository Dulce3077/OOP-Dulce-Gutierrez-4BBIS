DB_CONFIG = {
    'host': 'localhost',
    'database': 'login_system_db',
    'user': 'postgres',       
    'password': 'Dm061001',
    'port': 5432
}

import psycopg2
from psycopg2 import Error
from Controller.config import DB_CONFIG
class Database_connection:
    def __init__(self):
        self.config = DB_CONFIG

    def obtener_conexion(self):
        try:
            conexion = psycopg2.connect(**self.config)
            return conexion
        except Error as e:
            print(f"Error al conectar con PostgreSQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=None):
        conexion = self.obtener_conexion()
        if not conexion:
            return None
        
        cursor = None
        try:
            import psycopg2.extras
            cursor = conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute(query, params)
            
            if query.strip().upper().startswith("SELECT"):
                resultados = cursor.fetchall()
                return resultados
            else:
                conexion.commit()
                return cursor.rowcount
                
        except Error as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
