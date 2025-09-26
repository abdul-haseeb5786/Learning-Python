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

# Explicit
print("\n--- Explicit Type Conversion ---")
print(int(7.8))        # float → int
print(float(9))        # int → float
print(int("45"))       # string → int
print(str(45))         # int → string
print(str(6.7))        # float → string
print(float("6.7"))    # string → float
print(bool(0))         # int → bool
print(int(False))      # bool → int
print(complex(5))      # int → complex

# Invalid conversion (will raise error)
# print(int("Karachi"))

# ================================
# LITERALS
# ================================
print("\n--- Literals ---")
# Numeric
a = 0b1010  # binary
b = 100     # decimal
c = 0o310   # octal
d = 0x12c   # hexa
print(a, b, c, d)

# Float & complex
float_1 = 100.5
float_2 = 1.5e2
float_3 = 4.6e-3
x = 2.4j
print(float_1, float_2, float_3)
print(x, x.real, x.imag)

# String
string = "I am Abdullah"
multiline_str = """This is
a multiline string"""
unicode_str = u"\U0001f600" # 😀
raw_str = r"raw \n string"
print(string)
print(multiline_str)
print(unicode_str)
print(raw_str)

# Boolean
a = True + 9
b = False + 4
print(a, b)
