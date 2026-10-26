import tkinter as tk
from tkinter import messagebox

class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        # PERSONALIZAR 1:
        # Cambia el título de la ventana.
        self.ventana.title("REGISTRO DE USUARIOS")

        # PERSONALIZAR 2:
        # Modifica las dimensiones de la ventana.
        self.ventana.geometry("420x440")

        # PERSONALIZAR 3:
        # Cambia el color de fondo.
        self.ventana.configure(bg="#D489AF")

        self.ventana.resizable(False, False)

        # Mantiene la ventana asociada a la principal.
        self.ventana.transient(root)
        self.ventana.grab_set()

        # PERSONALIZAR 4:
        # Cambia el título, la fuente y sus colores.
        self.titulo = tk.Label(
            self.ventana,
            text="CREAR CUENTA",
            font=("Arial", 19, "bold"),
            bg="#29BEA3",
            fg="#2D4671"
        )
        self.titulo.pack(pady=18)

        # PERSONALIZAR 5:
        # Modifica el texto y estilo de las etiquetas.
        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg="#CAF0E9",
            font=("Arial", 10)
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=35,
            font=("Arial", 10)
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Correo electrónico:",
            bg="#CAF0E9",
            font=("Arial", 10)
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=35,
            font=("Arial", 10)
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña:",
            bg="#CAF0E9",
            font=("Arial", 10)
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Arial", 10)
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg="#CAF0E9",
            font=("Arial", 10)
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Arial", 10)
        )
        self.entry_confirmar.pack(pady=4)

        # PERSONALIZAR 6:
        # Cambia el texto, color, fuente y tamaño del botón.
        self.btn_guardar = tk.Button(
            self.ventana,
            text="Registrar usuario",
            width=22,
            bg="#853EA7",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=12)

        # Botón para cancelar el registro.
        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=22,
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()