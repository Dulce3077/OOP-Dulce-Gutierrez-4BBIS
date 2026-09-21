class pencil_case:
  def __init__(self, color, shape, material):
    self.color = color
    self.shape = shape
    self.material = material

  def close(self):
    print("The pencil case is closed")

  def open(self):
    print("The pencil case is open")

  def describe(self):
    print(f"This pencil case is made with {self.material}", f"the color of this pencil case is {self.color}")

#self: se utiliza para decirle a python a que un objeto pertenecen los atributos
#Create an instance using the class "table"

pencil_case1 = pencil_case("blue", "Rectangular", "fabric")
pencil_case2 = pencil_case("lilac", "square", "plastic")


#We access to the object(Intance "table 1" to call itds data)

print(pencil_case1.material)
print(pencil_case2.color)
pencil_case1.open()
pencil_case2.close()

#Intance "table 2"
print(pencil_case2.material)




class BankAccount:
  def __init__(self, holder, balance):
    self.holder = holder
    self.__balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.__balance = self.__balance + amount
      print("Deposit successful")
    else:
      print("The amount must be greater than 0")

  def withdraw(self, amount):
    if amount > self.__balance:
      print("Insufficient balance")
    elif amount <= 0:
      print("The amount must be greater than 0")
    else:
      self.__balance = self.__balance - amount
      print("Withdrawal successful")

  def check_balance(self):
    print(f"Current balance: ${self.__balance}")


# Create the accounts
account1 = BankAccount("Raúl Pérez", 5000)
account2 = BankAccount("Joel López", 3000)

# Account 1
print(account1.holder)
account1.check_balance()

account1.deposit(1000)
account1.withdraw(500)

account1.check_balance()

# Account 2
print(account2.holder)
account2.check_balance()

account2.deposit(500)
account2.withdraw(200)

account2.check_balance()