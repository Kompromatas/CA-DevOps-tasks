def hello (name):
    print(f"Hello {name} from module1!") 


class Animal:
    sound = "au au"

    def make_sound(self):
        print(self.sound)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.balance


class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        print(f"Car information: {self.year} {self.brand} {self.model} {self.color}")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} {self.color}"
    
    def __repr__(self):
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}')"