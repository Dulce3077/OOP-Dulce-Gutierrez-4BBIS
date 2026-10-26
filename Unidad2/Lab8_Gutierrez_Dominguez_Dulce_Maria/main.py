import tkinter as tk
from models.user import UserModel
from views.login_view import LoginView
from controllers.login_controller import Authentication

if __name__ == "__main__":
    # 1. Initialize the main window
    root = tk.Tk()
    
    # 2. Instantiate the Model (using your new PostgreSQL connection)
    modelo = UserModel()
    
    # 3. Instantiate the View
    vista = LoginView(root)
    
    # 4. Instantiate the Controller to connect Model and View
    app = Authentication(modelo, vista)
    
    # 5. Run the application loop
    root.mainloop()