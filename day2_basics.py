"""
Day 2 - Python Intermediate Practice:
- String manipulation
- Functions and scope
- File I/O
- Dictionaries and sets
- Debugging and testing
"""
# String slicing
name = "Thanabhum"
print(name[:5]) # Output: Thana

# Case change
print(name.upper())
print(name.lower())

# Replace & find
greeting = "Hello, world!"
print(greeting.replace("world", "Pooh"))
print("Pooh" in greeting)

# f-string formatting
age = 21
print(f"My name is {name} and I am {age} years old.")

def greet(person):
    message = f"Hi {person}!"
    return message

print(greet("Pooh"))

# Scope example
global_var = "outside"

def check_scope():
    global global_var
    global_var = "inside"
    print("Inside function:", global_var)

check_scope()
print("Outside function:", global_var)

# Write to file
with open("hello.txt", "w") as f:
    f.write("This is Day 2 of Python Challenge!")

# Read from file
with open("hello.txt", "r") as f:
    content = f.read()
    print("File says:", content)

def add(a, b):
    return a + b

print("Test 1:", add(2, 3) == 5)
print("Test 2:", add(0, 0) == 0)
print("Test 3:", add(-1, 1) == 0)