class Animal:
    def speak(self):
        return "I don't know what sound I make"
    
class Dog(Animal): 
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow!"

dog = Dog()
cat = Cat()

print(f"Dog says: {dog.speak()} and cat says: {cat.speak()}")