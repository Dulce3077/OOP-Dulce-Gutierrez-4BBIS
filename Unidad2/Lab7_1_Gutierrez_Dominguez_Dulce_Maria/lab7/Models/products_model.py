from Controller.database_connection import Database_connection

class Producto:
    def __init__(self, id=None, producto=None, precio=None, stock=None):
        self.id = id
        self.producto = producto
        self.precio = precio
        self.stock = stock
        self.db = Database_connection()

    def obtener_todos(self):
        query = "SELECT id, producto AS nombre, precio, stock FROM productos"
        resultado = self.db.ejecutar_consulta(query)
        print("RESULTADO DESDE LA BD:", resultado) 
        return resultado if resultado else []

    def guardar(self):
        query = "INSERT INTO productos (producto, precio, stock) VALUES (%s, %s, %s)"
        conexion = self.db.obtener_conexion()
        if not conexion:
            return False
        
        cursor = conexion.cursor()
        try:
            cursor.execute(query, (self.producto, self.precio, self.stock))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al guardar producto: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
