# -----------------------------
# Identity Operators
# -----------------------------
a = 3
b = 3

print(a is b)       # True (same memory location for small ints)
print(a is not b)   # False

x = "Hello"
y = "World"
print(x is y)       # False
print(x is not y)   # True

x = "Hello-world"
y = "Hello-world"
print(x is y)       # True (string interning)
print(x is not y)   # False

m = [1, 2, 3, 4]
n = [1, 2, 3, 4]
print(m is n)       # False (different objects in memory)
print(m == n)       # True (values are the same)
print(m is not n)   # True
