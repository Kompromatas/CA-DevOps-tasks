class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def peron_info(self):
        return f"{self.name} is {self.age} years old."

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def student_info(self):
        return f"{self.name} of age {self.age} has a grade in Python programing {self.grade}."

name = input("Enter person name: ")
age = int(input("Enter person age: "))
grade = input("Enter student grade: ") 

person = Person(name, age)
student = Student(name, age, grade)

print(f"Person info: {person.peron_info()}")

print(f"Student info: {student.student_info()}")   