from abc import ABC, abstractmethod
import os
import tkinter as tk
from tkinter import ttk


class SmartDevice(ABC):

  def __init__(self, name: str):
    self.name = name

  @abstractmethod
  def turn_on(self) -> str:
    pass

  @abstractmethod
  def turn_off(self) -> str:
    pass


class SmartTV(SmartDevice):

  def __init__(self):
    super().__init__("TV 1")

  def turn_on(self) -> str:
    return f"{self.name} is playing Netflix"

  def turn_off(self) -> str:
    return f"{self.name} is off."


class SmartAC(SmartDevice):

  def __init__(self):
    super().__init__("AC 1")

  def turn_on(self) -> str:
    return f"{self.name} is currently ON at 25°C"

  def turn_off(self) -> str:
    return f"{self.name} is OFF"


class SmartLamp(SmartDevice):

  def __init__(self):
    super().__init__("Lamp 1")

  def turn_on(self) -> str:
    return f"{self.name} is ON at medium"

  def turn_off(self) -> str:
    return f"{self.name} is OFF"


class SmartDoor(SmartDevice):

  def __init__(self):
    super().__init__("Door 1")

  def turn_on(self) -> str:
    return f"{self.name} is unlocked."

  def turn_off(self) -> str:
    return f"{self.name} is locked"


class SmartHomeApp(tk.Tk):

  def __init__(self):
    super().__init__()

    # --- 1. WINDOW SETTINGS---
    self.title("Lab 6: Polymorphism GUI by Dulce Maria Gutierrez Dominguez")
    self.geometry("480x520")  # Aumentado para dar espacio al Log
    self.resizable(True, True)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_dir = os.path.join(current_dir, "app_icon.png")

    if os.path.exists(icon_dir):
      self.app_icon = tk.PhotoImage(file=icon_dir)
      self.iconphoto(True, self.app_icon)
    else:
      print("The file doesn't exist")

    # --- 2. OBJECT REGISTRY---
    self.items = {
        "Smart TV": SmartTV(),
        "Smart AC": SmartAC(),
        "Smart Lamp": SmartLamp(),
        "Smart Door": SmartDoor(),
    }

    # Build visual components
    self._build_interface()

  def _build_interface(self):
    # Header / Title Banner
    lbl_header = tk.Label(
        self,
        text="Smart Home Center",
        font=("Times New Roman", 30, "bold"),
        fg="#2c3e50",
    )
    lbl_header.pack(pady=8)

    # Selection Group (Radiobuttons)
    group_box = tk.LabelFrame(
        self,
        text=" Select an Option ",
        font=("Times New Roman", 16, "bold"),
        padx=15,
        pady=5,
    )
    group_box.pack(fill="x", padx=20, pady=5)

    first_key = list(self.items.keys())[0]
    self.selected_key = tk.StringVar(value=first_key)

    for key in self.items.keys():
      rb = ttk.Radiobutton(
          group_box, text=key, value=key, variable=self.selected_key
      )
      rb.pack(anchor="w", pady=2)

    # Trigger Action Buttons
    btn_on = tk.Button(
        self,
        text="Turn On Device",
        command=lambda: self._handle_action("on"),
        bg="#2980b9",
        fg="white",
        font=("Times New Roman", 16, "bold"),
        relief="raised",
        cursor="hand2",
        padx=10,
        pady=4,
    )
    btn_on.pack(pady=8)

    btn_off = tk.Button(
        self,
        text="Turn Off Device",
        command=lambda: self._handle_action("off"),
        bg="#b93029",
        fg="white",
        font=("Times New Roman", 16, "bold"),
        relief="raised",
        cursor="hand2",
        padx=10,
        pady=4,
    )
    btn_off.pack(pady=4)

    # Output / Results Box
    self.lbl_output = tk.Label(
        self,
        text="Select an option above and click an action button.",
        font=("Times New Roman", 10, "italic"),
        bg="#ecf0f1",
        fg="#34495e",
        relief="groove",
        height=2,
        wraplength=420,
        justify="center",
    )
    self.lbl_output.pack(fill="x", padx=20, pady=5)

    # --- AQUÍ AGREGAS TU ACTIVITY LOG ---
    log_frame = tk.LabelFrame(
        self, text=" Activity Log ", font=("Arial", 11, "bold")
    )
    log_frame.pack(fill="both", expand=True, padx=20, pady=10)

    self.log_list = tk.Listbox(log_frame, height=5, font=("Consolas", 10))
    self.log_list.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(log_frame, command=self.log_list.yview)
    scrollbar.pack(side="right", fill="y")
    self.log_list.config(yscrollcommand=scrollbar.set)

  def _handle_action(self, action: str):
    chosen_key = self.selected_key.get()
    active_object: SmartDevice = self.items[chosen_key]

    if action == "on":
      result_message = active_object.turn_on()
    else:
      result_message = active_object.turn_off()

    # 1. Mostrar resultado en la etiqueta superior
    self.lbl_output.config(
        text=result_message, font=("Times New Roman", 10, "normal")
    )

    # 2. Agregar el evento al Activity Log
    self.log_list.insert(tk.END, result_message)
    self.log_list.see(tk.END)  # Hace scroll automático hacia el último registro


# LAUNCHER
if __name__ == "__main__":
  app = SmartHomeApp()
  app.mainloop()