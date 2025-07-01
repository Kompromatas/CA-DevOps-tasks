from module1 import Rectangle

width = float(input("Enter width: "))
height = float(input("Enter height: "))

S = Rectangle(width, height).area()
P = Rectangle(width, height).perimeter()

print(f"Area: {S}")
print(f"Perimeter: {P}")