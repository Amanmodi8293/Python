class Employee:
        company = "Apple"
        def show(self):
            print(f"The name is {self.name} and company is {self.company}")
        @classmethod
        def changeCompany(cls, newCompany):
            cls.company = newCompany

e = Employee()
e.name = "Amanmodi"
e.show()
e.changeCompany("Tesla")
e.show()
print(Employee.company)
print(e.company)