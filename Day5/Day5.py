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











































