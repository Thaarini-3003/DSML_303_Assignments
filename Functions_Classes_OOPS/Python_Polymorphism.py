"""Method Overloading not supported in Python"""
"""It needs a little work around"""

# Method Overloading with same name but different no. of parameters

# First product method Takes two argument and print their product
def product(a, b):
    p = a * b
    print(p)

# Second product method Takes three argument and print their product
def product(a, b, c):
    p = a * b*c
    print("Recent method gets called", p)

# Uncommenting the below line shows an error. Python always calls the recent method
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)


#Method Overloading : Work Around in Python
"""We can use the arguments to make the same function work differently i.e. as per the arguments."""
# Function to take multiple arguments
def add(datatype, *args):

    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:

        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')


"""********************************************************************"""
""" Operator Overloading """
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print("Operator Overloading :", v3) # Output: (6, 8)


"""Constructor Overloading"""
class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age


# Example Usage
person1 = Person("Alice")
person2 = Person("Bob", 25)

# Output
print("*** Constructor Overloading ***")
print(person1.name, person1.age)
print(person2.name, person2.age)