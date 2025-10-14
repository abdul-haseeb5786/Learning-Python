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








