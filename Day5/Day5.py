# ==========================================================
# Day 5: String Operations, Lists, Tuples, and Sets in Python
# ==========================================================

# ----------------------------------------------------------
# 🔠 STRING OPERATIONS
# ----------------------------------------------------------

# Looping through strings
name = "Abdul Rehman"
for i in name:
    print(i)

# Common string functions
string = "Abdul Rehman"
print(len(string))
print(string.upper())
print(string.lower())
print(string.title())
print(string.swapcase())

# Finding and replacing
print(string.find("man"))
print(string.replace("Abdul", "Ali"))

# Splitting, joining, and formatting
print(string.split())
print(" ".join(["Abdul", "Rehman"]))
print("My name is {} and I am {} years old".format("Abdul Rehman", 20))
print("My name is {name} and I am {age} years old".format(name="Abdul Rehman", age=20))

# String tests
s = "Python3"
print(s.isalpha())    # False (contains number)
print(s.isalnum())    # True
print(s.isdigit())    # False
print(s.isdecimal())  # False
print(s.startswith("Py"))
print(s.endswith("3"))

# ----------------------------------------------------------
# 🧮 MUTABLE VS IMMUTABLE DATA TYPES
# ----------------------------------------------------------
# Mutable: list, dict, set
# Immutable: int, float, str, tuple

# ----------------------------------------------------------
# 🧾 LISTS
# ----------------------------------------------------------

# Creating lists
students = ["asad", "fawad", "mehmmod", "aleem", "abdul rehman"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 10, True, 20.5]

# Accessing list elements
print(students[0])
print(students[-1])
print(students[1:4])

# Editing elements
students[0] = "Ali"
students[2:4] = ["Zain", "Umair"]
print(students)

# Adding elements
students.append("New Student")
students.insert(2, "Inserted Student")
students.extend(["Ameen", "Umer"])
print(students)

# Deleting elements
del students[0]
students.remove("Ameen")
students.pop()
students.clear()
print(students)

# Operations
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
print(l1 * 2)
print(3 in l1)

# Functions
print(len(l1))
print(min(l1))
print(max(l1))
print(sum(l1))
print(sorted(l1, reverse=True))

# ----------------------------------------------------------
# 🧠 PRACTICE TASKS
# ----------------------------------------------------------

# Task 1: Capitalize each word without using title()
string = "hello how are you"
lst = [word.capitalize() for word in string.split()]
print(" ".join(lst))

# Task 2: Extract username from email
email = "abc@gmail.com"
print(email[:email.find("@")])

# Task 3: Remove duplicates without using set()
lst1 = [1,2,4,3,3,6,5,5,8,2,1,0,7,8,6,7]
unique = []
for i in lst1:
    if i not in unique:
        unique.append(i)
print(unique)

# ----------------------------------------------------------
# 🧱 TUPLES
# ----------------------------------------------------------

# Creating tuples
t1 = (1, 2, 3)
t2 = ("Ali", 25, True)
t3 = (1, 2, (3, 4, 5))
print(t1, t2, t3)

# Accessing tuple elements
print(t1[0])
print(t1[-1])
print(t3[2][1])

# Tuple type conversion
lst = [10, 20, 30]
tup = tuple(lst)
print(tup)

# Tuple operations
t4 = (1, 2, 3)
t5 = (4, 5, 6)
print(t4 + t5)
print(t4 * 2)

# Tuple functions
print(len(t4))
print(min(t4))
print(max(t4))
print(sum(t4))
print(sorted(t4, reverse=True))
print(t4.index(2))

# Tuple type conversion
lst = [10, 20, 30]
tup = tuple(lst)
print(tup)

# Tuple operations
t4 = (1, 2, 3)
t5 = (4, 5, 6)
print(t4 + t5)
print(t4 * 2)

# Tuple functions
print(len(t4))
print(min(t4))
print(max(t4))
print(sum(t4))
print(sorted(t4, reverse=True))
print(t4.index(2))

# ----------------------------------------------------------
# 🧩 SETS
# ----------------------------------------------------------

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1)
print(type(set1))

# Adding elements
set1.add(9)
set1.update([10, 11])
print(set1)

# Deleting elements
set1.remove(3)
set1.discard(12)  # no error if element not found
set1.pop()        # removes random element
print(set1)

# Set operations
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# Common functions
print(len(set1))
print(min(set1))
print(max(set1))
print(sum(set1))
print(sorted(set1, reverse=True))

# ----------------------------------------------------------
# 🏁 END OF DAY 5
# ----------------------------------------------------------
print("\n✅ Day 5 — Completed: Strings, Lists, Tuples, and Sets in Python ✅")
