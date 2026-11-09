import tkinter as tk
from Views.login_view import LoginVentana

def main():
    print("Iniciando aplicación...") 
    root = tk.Tk()
    print("Ventana Tkinter creada.") 
    app = LoginVentana(root)
    print("LoginVentana instanciada.") 
    root.mainloop()
    print("Aplicación cerrada.") 

if __name__ == "__main__":
    main()