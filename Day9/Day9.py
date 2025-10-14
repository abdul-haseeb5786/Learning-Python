# 🐍 Day 9: Object-Oriented Programming in Python (OOP)

# -------------------------------
# 🌟 Introduction to OOP
# -------------------------------
# OOP helps in building scalable, reusable, and maintainable applications.

# Advantages:
# - Clear structure
# - Reusability
# - DRY (Don’t Repeat Yourself)
# - Easier debugging

# Core Concepts:
# 1. Class
# 2. Object
# 3. Method
# 4. Encapsulation
# 5. Inheritance
# 6. Polymorphism
# 7. Abstraction


# -------------------------------
# 1️⃣ Class and Object
# -------------------------------

# Example
class MyClass:
    x = 5

# Create object
p1 = MyClass()
print(p1.x)

# -------------------------------
# 2️⃣ Class and Object Example
# -------------------------------
class student:
    # Data (Attributes)
    name = "Abdul Rehman"
    roll_no = 1020
    course = "Data Sciences"
    location = "Gulshan"

    # Methods (Behaviors)
    def study(self):
        print(f"{self.name} is studying")

    def exam(self):
        print(f"{self.name} is giving an exam")

    def fee(self):
        print(f"{self.name} has submitted the fee")

# Object
s1 = student()
print(s1.name, s1.roll_no, s1.course, s1.location)
s1.study()
s1.exam()
s1.fee()

# -------------------------------
# 3️⃣ Constructor (__init__)
# -------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name, p1.age)


# Example 2
class Teacher:
    def __init__(self, name, teach_class, school):
        self.name = name
        self.teach_class = teach_class
        self.school = school

    def names(self):
        print(f"My name is {self.name}")

    def teach(self):
        print(f"I am teaching class {self.teach_class}")

    def schools(self):
        print(f"I am from {self.school} school")

t1 = Teacher("Abdul Rehman", "AI & DS", "SMIT")
print(t1.name, t1.teach_class, t1.school)
t1.names()
t1.teach()
t1.schools()

# -------------------------------
# 4️⃣ ATM Project Example
# -------------------------------
class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello! How would you like to proceed?
        1. Create PIN
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye!")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("PIN set successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount: "))
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount: "))
            if self.balance >= amount:
                self.balance -= amount
                print("Withdraw Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Invalid PIN")


# Uncomment to test
# ubl = ATM()






