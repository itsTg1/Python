class Animal:
    def sound(self):
        return "speaking"

class Dog(Animal):
    def sound(self):
        return "bark"

class Cat(Animal):
    def sound(self):
        return "meow"

tommy=Dog()
print(tommy.sound())