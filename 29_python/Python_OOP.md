# Python Object-Oriented Programming (OOP) Guide

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code to manipulate that data. Python supports OOP, making it easy to model real-world entities.

## Key Concepts

### 1. Classes and Objects

- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!
```

### 2. Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

cat = Cat()
cat.speak()  # Output: Meow
```

### 3. Encapsulation

Encapsulation restricts direct access to some of an object's components.

```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

person = Person("Alice")
print(person.get_name())  # Output: Alice
```

### 4. Polymorphism

Polymorphism allows different classes to be treated as instances of the same class through a common interface.

```python
class Bird:
    def make_sound(self):
        print("Chirp")

class Duck(Bird):
    def make_sound(self):
        print("Quack")

def animal_sound(animal):
    animal.make_sound()

duck = Duck()
bird = Bird()
animal_sound(duck)  # Output: Quack
animal_sound(bird)  # Output: Chirp
```

## Summary

- **Classes** define the structure and behavior.
- **Objects** are instances of classes.
- **Inheritance** promotes code reuse.
- **Encapsulation** hides internal details.
- **Polymorphism** enables flexible code.

OOP helps organize code, making it more modular, reusable, and easier to maintain.
