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

# -------------------------------
# 5️⃣ Encapsulation
# -------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fredrick", 50000)
print(emp.name)
# print(emp.__salary)  # ❌ Error: private attribute


# -------------------------------
# 6️⃣ Inheritance
# -------------------------------
class User:
    def login(self):
        print("Login")
    def register(self):
        print("Register")

class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

s1 = Student()
s1.enroll()
s1.review()
s1.login()
s1.register()


# -------------------------------
# 7️⃣ Inheritance with super()
# -------------------------------
class Car:
    def __init__(self, seats, tyres, steering, brake, horn, car_name):
        self.seats = seats
        self.tyres = tyres
        self.steering = steering
        self.brake = brake
        self.horn = horn
        self.car_name = car_name

    def speed(self):
        print(f"The {self.car_name} is running")

    def describe_car(self):
        print(f"""
        Car Model: {self.car_name}
        Seats: {self.seats}
        Tyres: {self.tyres}
        Horn: {self.horn}
        Steering: {self.steering}
        Brake: {self.brake}
        """)

class ElectricCar(Car):
    def __init__(self, make, model, year, engine, seats, tyres, steering, brake, horn, car_name):
        super().__init__(seats, tyres, steering, brake, horn, car_name)
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def describe_electric_car(self):
        print(f"""
        Company: {self.make}
        Model: {self.model}
        Year: {self.year}
        Engine: {self.engine}
        """)

e1 = ElectricCar('Tesla', 'ES01', 2021, 'Erc20', 4, 4, 'Right', 'ABS', 'Light', 'Model X')
e1.speed()
e1.describe_car()
e1.describe_electric_car()


# -------------------------------
# 8️⃣ Polymorphism
# -------------------------------
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.sound()


# -------------------------------
# 9️⃣ Abstraction
# -------------------------------
from abc import ABC, abstractmethod

class BankApp(ABC):
    def database(self):
        print("Connected to database")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        print("Login to mobile")

    def security(self):
        print("Mobile security")

mob = MobileApp()
mob.database()
mob.mobile_login()
mob.security()


# -------------------------------
# 🔟 Magic Methods
# -------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2
print(result.x, result.y)


# Override Magic Methods
class CarMagic:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def __str__(self):
        return "The object has been initialized"

    def __sizeof__(self):
        return "The size of object in bytes"

c = CarMagic(8, 9, "Gas")
print(c)
print(c.__sizeof__())
