class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 2 * 3.14 * self.radius

width = int(input("Enter rectangle width: "))
height = int(input("Enter rectangle height: "))
radius = int(input("Enter circle radius: "))

rectangle = Rectangle(width, height)
circle = Circle(radius)

print(f"Rectangle area is {rectangle.area()} and perimeter is {rectangle.perimeter()}")
print(f"Circle area is {circle.area()} and perimeter is {circle.perimeter()}")