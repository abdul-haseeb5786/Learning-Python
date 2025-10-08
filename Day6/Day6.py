# Day 6: Python Functions
# Created by: Abdul Rehman
# Last Edited: 28-08-25

# -----------------------------
# Introduction to Functions
# -----------------------------
# A function is a reusable block of code that performs a specific task.

# Benefits:
# 1. Modularity – Code is broken into smaller, manageable pieces.
# 2. Reusability – Write once, use many times.
# 3. Readability – Code becomes more organized and easy to maintain.

# -----------------------------
# Example Function
# -----------------------------
def is_even(num):
    '''
    Function gives odd or even.
    Input : valid integer
    Output : 'Odd' or 'Even'
    Created by : Abdul Rehman
    Last Edit : 28-8-25
    '''
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# Function call examples
print(is_even(6))

for i in range(10):
    print(is_even(i))

# Accessing function documentation
print(is_even.__doc__)

# -----------------------------
# Difference between return and print
# -----------------------------
# print -> Displays output on screen (not reusable)
# return -> Sends result back to caller (reusable)


# -----------------------------
# Parameters vs Arguments
# -----------------------------
# Parameter = Placeholder variable in function definition
# Argument  = Actual value passed when calling the function


# -----------------------------
# Example Functions
# -----------------------------
def power(a, b):
    return a ** b


print(power(5, 6))  # Normal function call

# Crashing example (missing argument)
# power(5)  # Uncomment to see error


# -----------------------------
# Default Arguments
# -----------------------------
def power(a=1, b=1):
    return a ** b


print(power(2, 4))   # Both arguments given
print(power(4))      

def greet(name='Guest'):
    print(f"Hello {name}")


greet("Abdul")
greet()

# -----------------------------
# Positional Arguments
# -----------------------------
print(power(2, 3))  # a=2, b=3


# -----------------------------
# Keyword Arguments
# -----------------------------
print(power(b=2, a=3))  # order doesn't matter when using keywords


# -----------------------------
# Arbitrary Positional Arguments (*args)
# -----------------------------
def flexible(*numbers):
    product = 1
    print(numbers)
    print(type(numbers))
    for i in numbers:
        product *= i
    print(product)


print(flexible(1, 2, 3))






























