# Day 7: Lambda Functions and Higher Order Functions

# ===============================
# Calculator Function
# ===============================
def calculator(arr, task):
    if task == 'add':
        total = 0
        for add in arr:
            total = total + add
        return total

    elif task == 'sub':
        total = 0
        for sub in arr:
            total = sub - total
        return total

    elif task == 'mul':
        total = 1
        for mul in arr:
            total = total * mul
        return total

    elif task == 'div':
        total = 1
        for div in arr:
            total = div / total
        return total

    elif task == 'exponent':
        power = int(input("Enter a power: "))
        return [sqr ** power for sqr in arr]

    elif task == 'avg':
        total = 0
        for avg in arr:
            total = total + avg
        return total / len(arr)

    elif task == 'even':
        evenlist = []
        for even in arr:
            if even % 2 == 0:
                evenlist.append(even)
        return evenlist

    elif task == 'odd':
        oddlist = []
        for odd in arr:
            if odd % 2 == 1:
                oddlist.append(odd)
        return oddlist

    else:
        return arr


# Example Calculator Calls
print(calculator([2, 3, 4, 5, 6, 7], 'add'))
print(calculator([2, 3, 4, 5, 6], 'sub'))
print(calculator([2, 3, 4, 5, 6, 7], 'mul'))
print(calculator([2, 3, 5, 6], 'div'))
print(calculator([2, 3, 4, 5, 6, 7], 'exponent'))
print(calculator([2, 3, 4, 5, 6, 7], 'avg'))
print(calculator([2, 3, 4, 5, 6, 7], 'odd'))
print(calculator([2, 3, 4, 5, 6, 7], 'even'))


# ===============================
# Function Examples
# ===============================
names = {'Abdullah', 'Abdul Rehman', 'Ameen', 'Aman', 'Ali', 'Owais'}

def person_name():
    for name in names:
        print(name)

person_name()


def build_person(first_name, last_name, age=''):
    person = {"First name": first_name, "Last_name": last_name}
    if age:
        person['age'] = age
    return person

print(build_person('Abdul', 'Rehman', '20'))
print(build_person('Abdullah', 'Zeeshan', 16))


def pizza(*toppings):
    for top in toppings:
        print(top)

pizza('pappareno', 'double chees')
pizza('extra chicken')


def build_profile(first, last, **user_profile):
    profile = {}
    profile['First name'] = first
    profile['Last name'] = last
    for key, value in user_profile.items():
        profile[key] = value
    return profile

print(build_profile('Abdul', 'Rehman'))
print(build_profile('Abdul', 'Rehman', education='Graduation', University='FAUUST'))


# ===============================
# Lambda Functions
# ===============================
# Syntax: lambda input: expression

x = lambda x: x ** 2
print(x(9))

a = lambda x, y: x + y
print(a(4, 7))
print(type(a))

# Lambda usage examples
a = lambda x: x[0] == "a"
print(a("apple"))
print(a("banana"))

b = lambda x: print("Even") if x % 2 == 0 else print("Odd")
b(6)

# ===============================
# Higher Order Functions (HOFs)
# ===============================
# Normal version
l = [11, 14, 21, 23, 56, 78, 45, 29, 28, 27, 15, 9]

def return_sum(l):
    even_sum = 0
    odd_sum = 0
    div3_sum = 0

    for i in l:
        if i % 2 == 0:
            even_sum = even_sum + i
        if i % 2 == 1:
            odd_sum = odd_sum + i
        if i % 3 == 0:
            div3_sum = div3_sum + i
    return even_sum, odd_sum, div3_sum

print(return_sum(l))


# HOF version
def return_sum(func, l):
    result = 0
    for i in l:
        if func(i):
            result = result + i
    return result

x = lambda x: x % 2 == 0
y = lambda x: x % 2 == 1
z = lambda x: x % 3 == 0

print(return_sum(x, l))
print(return_sum(y, l))
print(return_sum(z, l))


# ===============================
# Built-in Higher Order Functions
# ===============================
# MAP
l = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: x * 2, l)))

students = [
    {'name': 'Abdul Rehman', 'score': 90},
    {'name': 'Abdullah Zeeshan', 'score': 80},
    {'name': 'Ameen', 'score': 70}
]
print(list(map(lambda x: x['name'], students)))


# FILTER
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x > 4, l)))

names = ['ali', 'ameen', 'akib', 'zeeshan', 'ahmed', 'saleem']
print(list(filter(lambda i: 'e' in i, names)))


# REDUCE
from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x, y: x + y, l))         # Sum
print(reduce(lambda x, y: x if x > y else y, l))  # Max
print(reduce(lambda x, y: x if x < y else y, l))  # Min
print(reduce(lambda x, y: x * y, l))         # Product

