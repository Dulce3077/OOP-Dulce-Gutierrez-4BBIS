import tkinter as tk
from tkinter import ttk, messagebox
from Models.products_model import Producto

class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal - Sistema")
        self.root.geometry("750x450")
        
        self.root.configure(bg="#3B3B3D")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#3B3B3D", borderwidth=0)
        style.configure("TNotebook.Tab", background="#2B2B2D", foreground="white", padding=[10, 5], font=("Helvetica", 10, "bold"))
        style.map("TNotebook.Tab", background=[("selected", "#D88D34")], foreground=[("selected", "white")])

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_inicio = tk.Frame(self.notebook, bg="#3B3B3D")
        self.notebook.add(self.tab_inicio, text=" Inicio ")
        self.crear_pestana_inicio(nombre_usuario)

        self.tab_inventario = tk.Frame(self.notebook, bg="#3B3B3D")
        self.notebook.add(self.tab_inventario, text=" Inventario de Productos ")
        self.crear_pestana_inventario()

    def crear_pestana_inicio(self, nombre_usuario):
        lbl_mensaje = tk.Label(
            self.tab_inicio,
            text=f"Bienvenido/a, {nombre_usuario}",
            font=("Helvetica", 14, "bold"),
            bg="#3B3B3D",
            fg="#FFFFFF",
            justify="center"
        )
        lbl_mensaje.pack(pady=40)

        lbl_sub = tk.Label(
            self.tab_inicio,
            text="Utiliza las pestañas superiores para navegar por el sistema.",
            font=("Helvetica", 11),
            bg="#3B3B3D",
            fg="#CCCCCC"
        )
        lbl_sub.pack(pady=10)

        btn_salir = tk.Button(
            self.tab_inicio,
            text="Cerrar Sesión",
            font=("Helvetica", 11, "bold"),
            bg="#D88D34",
            fg="white",
            relief="flat",
            cursor="hand2",
            activebackground="#C07C2F",
            command=self.root.destroy
        )
        btn_salir.pack(pady=30, ipadx=10, ipady=5)

    def crear_pestana_inventario(self):
        lbl_titulo = tk.Label(
            self.tab_inventario,
            text="Listado de Productos en Inventario",
            font=("Helvetica", 13, "bold"),
            bg="#3B3B3D",
            fg="#FFFFFF"
        )
        lbl_titulo.pack(pady=10)

        frame_tabla = tk.Frame(self.tab_inventario, bg="#3B3B3D")
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=10)

        columnas = ("ID", "Nombre", "Precio", "Stock")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio ($)")
        self.tree.heading("Stock", text="Stock")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nombre", width=220, anchor="w")
        self.tree.column("Precio", width=100, anchor="e")
        self.tree.column("Stock", width=80, anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        btn_actualizar = tk.Button(
            self.tab_inventario,
            text="Actualizar Tabla",
            font=("Helvetica", 10, "bold"),
            bg="#D88D34",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.cargar_datos_db
        )
        btn_actualizar.pack(pady=10, ipadx=10, ipady=3)

        self.cargar_datos_db()

    def cargar_datos_db(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        try:
            prod_model = Producto()
            registros = prod_model.obtener_todos()

            if registros:
                for reg in registros:
                    self.tree.insert("", "end", values=(reg['id'], reg['nombre'], reg['precio'], reg['stock']))

        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo cargar la información:\n{e}")