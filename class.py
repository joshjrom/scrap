class Employee:
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = f"{firstName}.{lastName}@jromtech.com"

    def fullName(self):
        return f"{self.firstName} {self.lastName}"


emp_1 = Employee ("Joshua", "Ayegba", 50000)
emp_2 = Employee ("John", "Ayegba", "60000")


print(Employee.fullName(emp_1))
print(emp_1.fullName())