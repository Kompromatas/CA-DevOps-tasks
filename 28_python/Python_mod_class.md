# Python Classes: Creation and Usage

This guide explains how to create and use classes in Python, with examples and explanations.

## What is a Class?

A **class** is a blueprint for creating objects. It defines attributes (data) and methods (functions) that its objects will have.

## Creating a Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")
```

- `class Dog:` defines a new class named `Dog`.
- `__init__` is the constructor method, called when a new object is created.
- `self` refers to the instance of the class.
- `bark` is a method that prints a message.

## Creating Objects

```python
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Buddy says woof!
```

## Adding More Methods

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age}.")
```

## Inheritance

Classes can inherit from other classes.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow!")

my_cat = Cat()
my_cat.speak()  # Output: Meow!
```

## Summary

- Classes group data and behavior.
- Use `__init__` for initialization.
- Create objects by calling the class.
- Inheritance allows code reuse.

For more, see the [Python docs on classes](https://docs.python.org/3/tutorial/classes.html).