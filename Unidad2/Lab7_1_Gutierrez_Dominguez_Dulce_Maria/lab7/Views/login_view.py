import tkinter as tk
from tkinter import messagebox
from Models.login_model import User
from Views.home_view import DashboardVentana
from PIL import Image, ImageTk

class LoginVentana:
    
    def __init__(self, root):
        self.root = root
        self.root.title(" Acceso al Sistema ")
        self.root.geometry("350x520")
        self.root.resizable(False, False)
        
        self.root.configure(bg="#3B3B3D")

        self.logo_img = None

        self._crear_interfaz()

    def crear_logo(self):
        try:
            imagen_pil = Image.open("C:/Users/Usuario/Documents/UTD/4 CUATRIMESTRE/Programacion orientada a objetos/lab7 2_dulce_gutierrez/lab7/Assets/imagen.png")  
            imagen_pil = imagen_pil.resize((80, 80), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(imagen_pil)
            
            lbl_logo = tk.Label(self.root, image=self.logo_img, bg="#3B3B3D", bd=0)
            lbl_logo.pack(pady=5)
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
            lbl_logo = tk.Label(self.root, text="[ LOGO ]", font=("Helvetica", 12, "italic"), fg="gray", bg="#3B3B3D")
            lbl_logo.pack(pady=10)

    def _crear_interfaz(self):
        self.crear_logo()

        lbl_titulo = tk.Label(
            self.root, 
            text=" Iniciar Sesión ", 
            font=("Helvetica", 16, "bold"),
            bg="#3B3B3D",
            fg="#FFFFFF"
        )
        lbl_titulo.pack(pady=10)

        lbl_usuario = tk.Label(
            self.root, 
            text="Usuario:", 
            font=("Helvetica", 10, "bold"),
            bg="#3B3B3D",
            fg="#E0E0E0"
        )
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11), bg="#FFFFFF", fg="#333333", relief="solid", bd=1)
        self.entry_usuario.pack(fill="x", padx=30)

        lbl_pass = tk.Label(
            self.root, 
            text="Contraseña:", 
            font=("Helvetica", 10, "bold"),
            bg="#3B3B3D",
            fg="#E0E0E0"
        )
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        
        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*", bg="#FFFFFF", fg="#333333", relief="solid", bd=1)
        self.entry_pass.pack(fill="x", padx=30)

        btn_ingresar = tk.Button(
            self.root, 
            text="Entrar ", 
            font=("Helvetica", 11, "bold"),
            bg="#D88D34", 
            fg="white", 
            relief="flat",
            cursor="hand2",
            command=self.validar_login,
            activebackground="#C07C2F" 
        )
        btn_ingresar.pack(fill="x", padx=30, pady=25, ipady=3)

    def validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario and len(datos_usuario) > 0:
            usuario_encontrado = datos_usuario[0]
            nombre_usuario = usuario_encontrado.get('nombre', 'Usuario')
            
            messagebox.showinfo("Bienvenido", f"¡Hola {nombre_usuario}! Acceso concedido ")
            self._abrir_dashboard(nombre_usuario)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_dashboard = tk.Tk()
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()