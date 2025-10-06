# Loops
# Loop is the method of programming which is used for the work that you want to repeat again and again.

# Two types of loops in Python:
# 1. While Loop
# 2. For Loop

# ======================
# While Loop Examples
# ======================

# Syntax
'''
while condition:
    code
'''

i = 1
while i < 6:
    print(i)
    i += 1

name = "Abdul Rehman"
i = 1
while i <= 10:
    print(name)
    i += 1

num = int(input("Enter the table: "))
i = 1
while i <= 10:
    print(i * num)
    i += 1

table = int(input("Enter the Table: "))
rng = int(input("Enter the range: "))

i = 1
while i <= rng:
    print(f"{table} x {i} = {i * table}")

# while loop with else
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("i is no longer less than 
    i += 1

# Backward loop
i = 10
while i >= 0:
    print(i)
    i -= 1

# Task: Table in backward direction
table = int(input("Enter table for backward loop: "))
i = 10
while i >= 1:
    print(f"{table} x {i} = {table * i}")
    i -= 1

    # Even numbers
print("Even numbers")
count = 0
while count < 20:
    if count % 2 == 0:
        print(count)
    count += 1

# Odd numbers
print("Odd numbers")
count = 0
while count < 20:
    if count % 2 == 1:
        print(count)
    count += 1

# Program for guessing the number
import random

jackpot = random.randint(1, 100)
guess = int(input("Enter the number: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess = int(input("Enter the number: "))
    counter += 1

print("Right Answer 🎉")
print(f"Total Attempts: {counter}")

# ======================
# For Loop Examples
# ======================

print(list(range(1, 11)))       # [1,2,3,...,10]
print(list(range(5)))           # [0,1,2,3,4]
print(list(range(1, 11, 2)))    # step of 2
print(list(range(10, 0, -1)))   # backward

for i in range(1, 10):
    print(i)

for i in range(10, 0, -1):
    print(i)

# Looping over a string
for i in "Islamabad":
    print(i)

for i in "Islamabad":
    print(i, end="")

for i in range(1, 20, 2):
    print(i)

# Note:
# When you know how many times the loop will run, use 'for loop'.
# If you don’t know, use 'while loop' (like guessing game).

# ======================
# Break, Continue, Pass
# ======================

# Break
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# Continue
for i in range(1, 11):
    if i == 6:
        continue
    print(i)

# Pass
for i in range(1, 11):
    pass

# For loop with if condition
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for i in "Islamabad":
    if i == "a":
        continue
    print(i)

for i in range(1, 20):
    if i % 11 == 0:
        print(f"{i} is multiple of 11")
        break
    else:
        print(i)

# ======================
# Strings
# ======================

# Strings are sequence of characters.
# In Python, they are sequences of Unicode characters.

# Creating Strings
name_1 = 'Ameen'
name_2 = "Ali"
name_3 = """Abdullah"""

print(name_1)
print(name_2)
print(name_3)

# Indexing and Slicing
# Positive Indexing: Left to Right (0, 1, 2, ...)
# Negative Indexing: Right to Left (-1, -2, ...)

a = 'Hello'

# Positive Indexing
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# print(a[5])  # IndexError: string index out of range

# Negative Indexing
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
# print(a[-6])  # IndexError: string index out of range


