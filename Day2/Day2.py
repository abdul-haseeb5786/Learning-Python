# ================================
# STRING FORMATTING
# ================================
name = input("Enter your name: ")
age = int(input("Enter your age: "))
field = input("Enter your field: ")

print("Using format(): Dear your name is {}, your age is {} and you are a {} student.".format(name, age, field))
print(f"Using f-string: Dear your name is {name}, your age is {age} and you are a {field} student.")

# Math inside f-string
print(f"The price is {12*12} Dollars")
