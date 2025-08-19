# Pet management system

class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"name of pet {self.name} and age is {self.age}")
    
    def speak(self):
        print("this pet makes sound")

class Dog(Pet):
    def __init__(self,breed,name,age):
        super().__init__(name,age)
        self.breed=breed
    
    def speak(self):
        print("woof!")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def speak(self):
        print("Meow!")
    


dog1=Dog("german shepard","tommy",2)
cat1=Cat("kitty",1,"black")   