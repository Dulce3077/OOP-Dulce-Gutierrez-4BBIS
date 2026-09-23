class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_total(self):
        return self.precio


class ProductoElectronico(Producto):
    def calcular_total(self):
        return self.precio * 1.16


class ProductoRopa(Producto):
    def calcular_total(self):
        return self.precio * 1.08


class ProductoAlimento(Producto):
    def calcular_total(self):
        return self.precio


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self.productos:
            total += producto.calcular_total()

        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_pedido(self):
        print(f"\nPedido #{self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Estado: {self.estado}")

        print("\nProductos:")

        for producto in self.productos:
            print(
                f"- {producto.nombre}: "
                f"${producto.precio:.2f}"
            )

        print(f"\nTotal: ${self.calcular_total():.2f}")


# Programa principal

pedido = Pedido(1001, "Ana")

pedido.agregar_producto(
    ProductoElectronico("Laptop", 15000)
)

pedido.agregar_producto(
    ProductoRopa("Playera", 500)
)

pedido.agregar_producto(
    ProductoAlimento("Cereal", 100)
)

pedido.mostrar_pedido()

pedido.cambiar_estado("ENVIADO")

print("\nNuevo estado:", pedido.estado)
