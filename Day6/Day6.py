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
