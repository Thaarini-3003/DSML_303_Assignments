"""Basic string Functions"""

# 1. Slicing Operations
s = "Hello, World!"
print(s[2:6])
print(s[:5])
print(s[2:])
print(s[-5:-2])

# 2. Modify String
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("H", "J"))
print(s.split(",")) # returns ['Hello', ' World!']

# 3. String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

# 4. String Format
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# 5. Placeholders
price = 59
txt = f"The price is {price} dollars"
print(txt)

# 6. String startswith()
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# 7. String endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)


