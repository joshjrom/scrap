class Employee:
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f" {firstName}.{lastName}@company.com"
    
    def employeeEmail(self):
        print(f"Your email is {self.firstName}.{self.lastName}@jromtech.com")


class Mammal(Employee): 
    def cat(self):
        print("The cat is working")


emp1 = Employee("Joshua", "Ayegba", 60000)
cat1 = Mammal("cat1", "cat2", 5000)


cat1.employeeEmail()


         

