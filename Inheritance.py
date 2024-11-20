class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
    
    def showDetails(self):
        print(f"The id of Employee is : {self.id}")
        print(f"The name of Employee is : {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print(f"The default language is Python")

e1 = Programmer("Aman",456)
e1.showDetails()
e1.showLanguage()
e2 = Employee("Modi",686)
e2.showDetails()