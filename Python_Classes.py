"""Class : Creation, Initialization and Object creation in Python"""

# Create a class
class MyClass:
  x = 5

# Create Object for the class
p1 = MyClass()
print(p1.x)

# (__init__) : Initialize the values in a class
class Person:
  def __init__(self):
    self.name = "Thaarini"
    self.age = 35
    self.marks = 90

p1 = Person() #p1 is reference variable
print("Name: ", p1.name)
print("Age :", p1.age)
print("Marks :", p1.marks)


# Initialize the values by passing arguments
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def talk(self):
        print("Hello My Name is:",self.name)
        print("My Roll_no is:",self.roll_no)
        print("My Marks are:",self.marks)
s1=Student("Raman",101,80)
s1.talk()

class Student:
    def __init__(self,x,y,z):
        self.name= x
        self.roll_no= y
        self.marks= z
    def display(self):
        print("Student Name:{} \n Rollno:{} \n Marks:{}".format(self.name,self.roll_no,self.marks))
s1=Student("Joel",101,80)
s1.display()
s2=Student("Raman",102,100)
s2.display()

# constructor will execute only once per object
class Test:
    def __init__(self):
        print("Constructor execution...")
    def m1(self):
        print("Method execution...")
t1=Test()
t2=Test()
t3=Test()
t1.m1()

