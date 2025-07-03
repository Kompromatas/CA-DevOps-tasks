class encapsulate:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age


man = encapsulate("John", 25)
print(f"Name {man.get_name()} and age {man.get_age()}") 
man.set_name("JONAS")
man.set_age(45)
print(f"Name {man.get_name()} and age {man.get_age()}") 
    