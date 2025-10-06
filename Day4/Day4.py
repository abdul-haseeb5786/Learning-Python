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
    print("i is no longer less than 10")














    
    i += 1
