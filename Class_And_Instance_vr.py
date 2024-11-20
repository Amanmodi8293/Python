class Employee:
    companyName = "Apple"
    No_of_Employees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 2.3
        Employee.No_of_Employees += 1

    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.No_of_Employees} sized {self.companyName} is {self.raise_amount}")

    
emp1 = Employee("Aman")
# Employee.showDetails(emp1)
emp1.companyName = "Tata"
emp1.raise_amount = 4.5
emp1.showDetails()

emp2 = Employee("Modi")
# Employee.showDetails(emp1)
emp2.companyName = "Birla"
emp2.raise_amount = 45.5
emp2.showDetails()