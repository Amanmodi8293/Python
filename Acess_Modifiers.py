# Public Acess Modifier
class Employee:
    def __init__(self):
        self.name = "Amanmodi"

a = Employee()
print(a.name) # can be access directly. Because this is public.


# Private Acess Modifier
class Employee:
    def __init__(self):
        self.__name = "Amanmodi"

a = Employee()
# print(a.__name) # cannot be access directly. Because this is private.
print(a._Employee__name) # can be access indirectly. Because this is private.
# print(a.__dir__())

# Protected Acess Modifier
class Employee:
    def __init__(self):
        self._name = "Amanmodi"

a = Employee()
print(a._name) # can be access directly. Because this is protected.
print(dir(a))