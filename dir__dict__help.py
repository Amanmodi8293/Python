# x = [1,2,3,4]
# print("\n\nAs a list ",dir(x))
# print(x.index)
# x = (1,2,3,4)
# print("\n\nAs a tuple ",dir(x))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
    

p = person("Amanmodi", 23)
print(p.__dict__)

print(help(person))