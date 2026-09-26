class user:
    def __init__(self,id_user,name,password):
        self.id_user = id_user
        self.name = name
        self._password = password # Tiene guión bajo porque es un atributo privado

    def show_user_info(self):
        return f"{self.id} - {self.name}"
    
    