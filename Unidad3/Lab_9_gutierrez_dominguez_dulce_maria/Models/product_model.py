
from Controller.database_connection import Database_connection


class Product:

    def __init__(self):
        self.db = Database_connection()

    def obtener_productos(self):

        query = """
            SELECT id_product, product_name, price
            FROM products
            ORDER BY id_product
        """

        return self.db.ejecutar_consulta(query)

    def registrar_producto(self, nombre, precio):

        query = """
            INSERT INTO products (product_name, price)
            VALUES (%s, %s)
        """

        return self.db.ejecutar_comando(
            query,
            (nombre, precio)
        )
