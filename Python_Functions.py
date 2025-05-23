"""Functions in Python"""

# 1. Syntax for User-Defined functions
def function_name(parameters):
    print("Hello")
    return parameters


# Program 1;
def greetings():
    print("Hello from a function")
greetings()
greetings()
greetings()
greetings()
greetings()

#Function Type 1:
#Function without arguments and without return type
def add():
    a = 10
    b = 20
    print(a+b)
add()


#Function Type 2:
#Functions with arguments and without return type
def add1(a,b):
    print(a+b)
add1(123,456)


#Function Type 3:
#Functions without arguments and with return type
def add2():
    a = 100
    b = 200
    return a+b
result = add2()
print(result)


#Function Type 4:
#Functions with arguments and with return type
def add3(x, y):
    return x+y
result = add3(23,45)
print(result)


#Functions with multiple return values
def calculator(a,b):
    sum = a+b
    diff = a-b
    product = a*b
    quo = a/b
    return sum, diff,product,quo
result = calculator(1234,50)
for i in result:
    print(i)


#functions with variable arguments
def sum(*n):
    total = 0
    for i in n:
        total = total + i
        print("The Sum of Given Number is ", total)
sum()
sum(10,20)
sum(123,456)
sum(10,20,30,40,50)

def greetings(name,msg="Advanced Python Course"):
    print("Hello", name, "Welcome to",msg)
greetings('Raman','Python Course')#Positional Arguments
greetings(msg='Java Course',name='Sam')#Named Arguments