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

# ================================
# TYPE CONVERSION
# ================================
# Implicit
print("\n--- Implicit Type Conversion ---")
print(9 + 9.5)      # int + float
print(5 + 6+7j)     # int + complex
print(2.5 + 9 + 5j) # float + complex
