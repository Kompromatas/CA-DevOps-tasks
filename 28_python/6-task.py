from module1 import Car

car1 = Car("Audi", "80", 1985, "blue")
car2 = Car("BMW", "318is", 1993, "black")

car1.info()
car2.info()

print(f"Car str information: {car1.__str__()}")
print(f"Car repr information: {car2.__repr__()}")