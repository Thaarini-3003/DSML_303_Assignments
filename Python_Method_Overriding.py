"""Method Overriding"""

# Parent Class: Person
class Person1:
    # Constructor
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    # Parent's display method
    def display(self):
        print(self.name)
        print(self.id_number)

# Child Class: Employee
class Employee1(Person1):
    # Constructor
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)  # Calls Parent's constructor
        self.salary = salary
        self.post = post

    # Child's display method
    def display(self):    # Overriding method
        print(self.salary)
        print(self.post)

per = Person1("Murali", 202)
per.display()
emp = Employee1("Thaarini",101, 50000, "DataScientist")
emp.display()