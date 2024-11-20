class Person:
    name = "Amanmodi"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
a.name = "Modiaman"
b.name = "Chourasiya"
a.occupation = "Web Developer"
b.occupation = "App Developer"
a.info()
b.info()
# print(a.name, a.occupation)