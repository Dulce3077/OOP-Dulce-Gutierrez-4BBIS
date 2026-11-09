
import tkinter as tk
from tkinter import ttk
from Models.product_model import Product
from Controller.product_controller import ProductController

class DashboardVentana:
    """Ventana principal del sistema e inventario."""

    def __init__(self, root, nombre_usuario):

        self.root = root

        self.root.title("Panel Principal")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        lbl_mensaje = tk.Label(
            self.root,
            text=f"¡Bienvenido/a al Sistema!\nUsuario activo: {nombre_usuario}",
            font=("Helvetica", 12),
            justify="center"
        )
        lbl_mensaje.pack(pady=15)

        lbl_nombre = tk.Label(
            self.root,
            text="Nombre del producto:"
        )
        lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.root,
            width=40
        )
        self.entry_nombre.pack(pady=5)

        lbl_precio = tk.Label(
            self.root,
            text="Precio:"
        )
        lbl_precio.pack()

        self.entry_precio = tk.Entry(
            self.root,
            width=40
        )
        self.entry_precio.pack(pady=5)

        self.btn_registrar = ttk.Button(
            self.root,
            text="Registrar producto"
        )
        self.btn_registrar.pack(pady=10)

        self.tabla = ttk.Treeview(
            self.root,
            columns=("id", "nombre", "precio"),
            show="headings",
            height=10
        )

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Product Name")
        self.tabla.heading("precio", text="Price")

        self.tabla.column("id", width=70, anchor="center")
        self.tabla.column("nombre", width=300)
        self.tabla.column("precio", width=150, anchor="center")

        self.tabla.pack(pady=15)

        lbl_formato = tk.Label(
            self.root,
            text="Select export format:"
        )
        lbl_formato.pack(pady=5)

        self.cmb_formato = ttk.Combobox(
            self.root,
            values=["CSV", "TXT", "JSON", "PDF"],
            state="readonly",
            width=15
        )

        self.cmb_formato.set("CSV")
        self.cmb_formato.pack()

        self.btn_exportar = ttk.Button(
            self.root,
            text="Export Report"
        )
        self.btn_exportar.pack(pady=15)

        self.modelo = Product()

        self.controlador = ProductController(
            self.modelo,
            self
        )

    def mostrar_productos(self, productos):

        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        for producto in productos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto["id_product"],
                    producto["product_name"],
                    producto["price"]
                )
            )
        

    def limpiar_campos(self):

        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
