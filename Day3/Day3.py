# -----------------------------
# Identity Operators
# -----------------------------
a = 3
b = 3

print(a is b)       # True (same memory location for small ints)
print(a is not b)   # False

x = "Hello"
y = "World"
print(x is y)       # False
print(x is not y)   # True

x = "Hello-world"
y = "Hello-world"
print(x is y)       # True (string interning)
print(x is not y)   # False

m = [1, 2, 3, 4]
n = [1, 2, 3, 4]
print(m is n)       # False (different objects in memory)
print(m == n)       # True (values are the same)
print(m is not n)   # True

# -----------------------------
# Membership Operators
# -----------------------------
x = "Islamabad"
print("I" in x)       # True
print("s" not in x)   # False

x = [1, 2, 3, 4, 5]
print(3 in x)         # True
print(6 not in x)     # True

# -----------------------------
# Bitwise Operators
# -----------------------------
print(6 & 3)   # AND → 2
print(6 | 3)   # OR  → 7
print(~3)      # NOT → -4

# -----------------------------
# If-Else Statements
# -----------------------------
a = 330
b = 200
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# AND operator
a, b, c = 200, 33, 500
if a > b and c > a:
    print("Both conditions are True")

# OR operator
if a > b or a > c:
    print("At least one condition is True")

# Nested if
x = 8
if x > 10:
    print("Above 10,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("Less than 10")

# -----------------------------
# Marksheet Program
# -----------------------------
name = input("Enter your name: ")
sub1 = float(input("Enter Chemistry marks: "))
sub2 = float(input("Enter Physics marks: "))
sub3 = float(input("Enter Math marks: "))
sub4 = float(input("Enter English marks: "))
sub5 = float(input("Enter Urdu marks: "))

obtained_marks = sub1 + sub2 + sub3 + sub4 + sub5
total_marks = 500
percentage = (obtained_marks / total_marks) * 100

if 90 <= percentage <= 100:
    grade = "A+"
elif 80 <= percentage < 90:
    grade = "A"
elif 70 <= percentage < 80:
    grade = "B"
elif 60 <= percentage < 70:
    grade = "C"
elif 50 <= percentage < 60:
    grade = "D"
else:
    grade = "F"

print(f"""
          CITY PUBLIC SCHOOL

     Your name is: {name}
     Your Percentage is: {percentage:.2f}%
     Your Grade is: {grade}
""")

