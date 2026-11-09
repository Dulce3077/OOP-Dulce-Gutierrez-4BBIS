
from tkinter import messagebox, filedialog

from Models.product_model import Product

from exporters import (
    CSVExporter,
    TXTExporter,
    JSONExporter,
    PDFExporter
)


class ProductController:

    def __init__(self, modelo, vista):

        self.modelo = modelo
        self.vista = vista

        self.exportadores = {
            "CSV": CSVExporter,
            "TXT": TXTExporter,
            "JSON": JSONExporter,
            "PDF": PDFExporter
        }

        self.vista.btn_registrar.config(
            command=self.registrar_producto
        )

        self.vista.btn_exportar.config(
            command=self.exportar_productos
        )

        self.cargar_productos()

    def cargar_productos(self):

        productos = self.modelo.obtener_productos()

        if productos is None:

            messagebox.showerror(
                "Error",
                "No fue posible obtener los productos."
            )

            return

        self.vista.mostrar_productos(productos)

    def registrar_producto(self):

        nombre = self.vista.entry_nombre.get().strip()
        precio = self.vista.entry_precio.get().strip()

        if not nombre or not precio:

            messagebox.showwarning(
                "Campos vacíos",
                "Completa todos los campos."
            )

            return

        try:
            precio = float(precio)

            if precio < 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Precio inválido",
                "Ingresa un precio numérico válido."
            )

            return

        resultado = self.modelo.registrar_producto(
            nombre,
            precio
        )

        if resultado:

            messagebox.showinfo(
                "Éxito",
                "Producto registrado correctamente."
            )

            self.vista.limpiar_campos()
            self.cargar_productos()

        else:

            messagebox.showerror(
                "Error",
                "No fue posible registrar el producto."
            )

    def exportar_productos(self):

        formato = self.vista.cmb_formato.get()

        if not formato:

            messagebox.showwarning(
                "Formato",
                "Selecciona un formato de exportación."
            )

            return

        productos = self.modelo.obtener_productos()

        if productos is None:

            messagebox.showerror(
                "Error",
                "No fue posible consultar los productos."
            )

            return

        if not productos:

            messagebox.showwarning(
                "Inventario vacío",
                "No hay productos para exportar."
            )

            return

        extensiones = {
            "CSV": ".csv",
            "TXT": ".txt",
            "JSON": ".json",
            "PDF": ".pdf"
        }

        extension = extensiones[formato]

        file_path = filedialog.asksaveasfilename(
            title="Save Report",
            defaultextension=extension,
            filetypes=[
                (f"{formato} files", f"*{extension}")
            ]
        )

        if not file_path:
            return

        exportador = self.exportadores[formato]()

        try:

            exportador.export(productos, file_path)

            messagebox.showinfo(
                "Exportación exitosa",
                f"El archivo se generó correctamente:\n{file_path}"
            )

        except Exception as error:

            messagebox.showerror(
                "Error de exportación",
                f"No fue posible generar el archivo:\n{error}"
            )
