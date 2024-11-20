class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_Details(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def show_Details(self):
        Animal.show_Details(self)
        print(f"Breed : {self.breed}")

class GoldenRetriver(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed= "Golden Retriver")
        self.color = color
    
    def show_Details(self):
        Dog.show_Details(self)
        print(f"Color : {self.color}")
         
o = GoldenRetriver("tommy", "black")
o.show_Details()
print(GoldenRetriver.mro())