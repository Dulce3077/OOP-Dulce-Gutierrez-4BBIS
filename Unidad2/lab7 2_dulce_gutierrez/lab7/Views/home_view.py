# import tkinter as tk

# class DashboardVentana:
#     def __init__(self, root, nombre_usuario):
#         self.root = root
#         self.root.title("Panel Principal")
#         self.root.geometry("400x250")

#         lbl_mensaje = tk.Label(
#             self.root, 
#             text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{nombre_usuario}", 
#             font=("Helvetica", 20),
#             justify="center"
#         )
#         lbl_mensaje.pack(expand=True)

import tkinter as tk

class DashboardVentana:
    
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title(" The Dashboard ")
        self.root.geometry("450x320")
        
        self.root.configure(bg="#FFF0F3")
        self.root.resizable(False, False)

        lbl_mensaje = tk.Label(
            self.root,
            text=f"\n\n Usuario Activo: \n{nombre_usuario}",
            font=("Helvetica", 14, "bold"),
            bg="#FFF0F3",
            fg="#D63384", 
            justify="center"
        )
        lbl_mensaje.pack(expand=True, pady=20)

        btn_salir = tk.Button(
            self.root,
            text="Cerrar Sesión",
            font=("Helvetica", 11, "bold"),
            bg="#FF69B4",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.root.destroy
        )
        btn_salir.pack(pady=20, ipadx=10, ipady=5)