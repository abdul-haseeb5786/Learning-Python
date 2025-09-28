








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
