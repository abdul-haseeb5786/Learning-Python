




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


# -----------------------------
# Login Program
# -----------------------------
user_name = "Abdul Rehman"
user_password = "1234"  # better to store as string

name = input("Enter your name: ")

if name == user_name:
    password = input("Enter your password: ")
    if password == user_password:
        print("LOGIN APPROVED")
    else:
        print("Your password is invalid")
else:
    print("Your name is invalid")


# -----------------------------
# Find Greatest Number
# -----------------------------
a, b, c = 10, 20, 30

if a > b and a > c:
    print(f"{a} is greatest")
elif b > a and b > c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
