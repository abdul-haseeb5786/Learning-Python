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



















    
