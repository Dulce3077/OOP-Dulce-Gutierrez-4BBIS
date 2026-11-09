from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw
        self.db: Database_connection = Database_connection()

    def auth(self):
        query = """
            SELECT id_user, username, nombre
            FROM users
            WHERE username = %s AND passw = %s
        """
        resultado = self.db.ejecutar_consulta(query, (self.username, self.password))
        return resultado