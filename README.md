# 🐍 Python 30-Day Challenge

Hi, I’m Pooh! This is my personal 30-day Python coding challenge to improve my skills through hands-on learning and daily practice.

---

## 📅 Progress

| Day | Topic                        | Status     |
|-----|------------------------------|------------|
| 1   | List Comprehensions          | ✅ Done     |
| 2   | Strings, Functions, Files    | ✅ Done     |
| 3   | Modules & Error Handling     | ✅ Done     |
| 4   | Classes & OOP                | ✅ Done     |
| 5   | File I/O, CSV, and JSON      | ✅ Done     |

---

## 📂 Files

| File              | Description                                 |
|-------------------|---------------------------------------------|
| `list_comp.py`    | Day 1: List comprehension practice          |
| `day2_basics.py`  | Day 2: Strings, functions, file I/O, tests  |
| `utils.py`        | Day 3: Custom helper functions (module)     |
| `day3_main.py`    | Day 3: Testing modules and error handling   |
| `hello.txt`       | File created/written by Python              |
| `day4_oop.py`     | Day 4: Classes, objects, and inheritance    |
| `day5_files.py`   | Day 5: Working with files, CSV, and JSON    |
| `data.csv`        | CSV file read/written by Python             |
| `data.json`       | JSON file created by Python                 |

---

## ✅ What I’ve Learned

### 🧠 Day 1: List Comprehensions
- Fast and readable way to create lists
- Used filtering and conditions
```python
evens = [x for x in range(10) if x % 2 == 0]
```

---

### 🧠 Day 2: Strings, Functions, and Testing
- Practiced string slicing, formatting, and file writing
- Wrote functions and understood local vs global scope
- Used file I/O with `open()`, `write()`, and `read()`
- Performed simple unit-like tests using `==`

---

### 🧠 Day 3: Modules & Error Handling
- Learned how to organize code with multiple files (modules)
- Created helper functions in `utils.py`
- Imported and reused functions in `day3_main.py`
- Practiced exception handling using `try`, `except`, `finally`

---

### 🧠 Day 4: Object-Oriented Programming (OOP)

#### ✅ Part 1: Classes and Objects
- Defined custom classes using `class`
- Used the `__init__` constructor to create object attributes
- Wrote methods like `.speak()` that belong to objects
```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

dog = Animal("Dog", "Woof")
print(dog.speak())  # Dog says Woof
```

#### ✅ Part 2: Inheritance
- Created subclasses that inherit from a base class
- Used `super()` to call parent class constructors
- Extended base class behavior with new methods
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def fetch(self):
        return f"{self.name} is fetching!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak())  # Buddy says Woof
print(my_dog.fetch())  # Buddy is fetching!
```

---

### 🧠 Day 5: Files, CSV, and JSON

#### ✅ Text File I/O
- Opened files with `open()`, wrote and read lines
- Used context managers (`with open(...) as f:`) to auto-close files
```python
with open("hello.txt", "w") as f:
    f.write("Hello from Day 5!\n")
```

#### ✅ CSV Handling
- Read tabular data using the `csv` module
- Wrote CSV files with custom headers
```python
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Pooh", 100])
```

#### ✅ JSON Handling
- Serialized Python dictionaries to JSON
- Loaded JSON data into Python objects
```python
import json

data = {"robot": "A1", "status": "active"}
with open("data.json", "w") as f:
    json.dump(data, f)
```

#### 🤖 AI & Robotics Use Case
- Learned how to log sensor data in CSV format
- Stored robot configurations and AI model settings using JSON
- Practiced reading structured data for automation tasks

---

## 🚀 Next Steps
- Day 6: Explore functions and modules deeply
- Use functions to structure robotics simulation logic
- Keep refining Git & documentation habits

---

## 📌 Repo Info
- Author: [poohsted](https://github.com/poohsted)
- Started: June 2025
