# Print examples
print("Hello World!")
print(123)
print(1232.5)
print("Hello", "World")
print("Hello", 123, True)
print("Hello", "World", 123, sep="#")


# End parameter in print
print("Hello", end="\n")
print("World!", end="\n")
print(123)

# Complex number
print(5 + 6j)

# List
print([1, 2, "h"])

# Tuple
print((544, 'dfgdf', True))

# Set
print({"type", 2324, False})

# Dictionary
print({"Name": "Abdullah", "Roll No": 123})

# String examples
print('My name is Abdullah')
print("My name is" + " " + "Abdullah")
print('''Abdullah''')

# Type checking
print(type(123))
print(type(True))
print(type([1, 2, 3, 5]))

# Large integer
print(353242342223423525225235235235)

# Infinity examples
print(1e309)
print(1.7e309)

# Float + integer
print(123 + 3.56)

# Print function again
print("Hello")

# Variables
name = 5
print(name)
name = 6
print(name)

n1 = 3
n2 = 5
print(n1)
print(n2)

n1, n2, n3 = 5, 6, 9
print(n1, n2, n3)

a, b, c = 2, 3, 4
print(a, b, c)

a = b = c = 10
print(a, b, c)
a = b = c = 11
print(a, b, c)

# Python keywords
import keyword
print(keyword.kwlist)

__ = "Name"
print(__)

Abdul_ = 'Abdul'
print(Abdul_)

# Input examples
user_input = input("Enter something: ")
print(user_input)

name = float(input("Name: "))
print(name)
print(type(name))

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
result = num1 + num2
print(result)