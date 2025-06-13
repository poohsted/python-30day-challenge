# 🐍 Python 30-Day Challenge

Hi, I’m Pooh! This is my personal 30-day Python coding challenge to improve my skills through hands-on learning and daily practice.

---

## 📅 Progress

| Day | Topic                        | Status   |
|-----|------------------------------|----------|
| 1   | List Comprehensions          | ✅ Done  |
| 2   | Strings, Functions, Files    | ✅ Done  |
| 3   | Modules & Error Handling     | ✅ Done  |
| 4   | Classes & OOP                | ✅ Done  |
| 5   | File I/O, CSV, and JSON      | 🔜 Coming up |

---

## 📂 Files

| File            | Description                                |
|-----------------|--------------------------------------------|
| `list_comp.py`  | Day 1: List comprehension practice         |
| `day2_basics.py`| Day 2: Strings, functions, file I/O, tests |
| `utils.py`      | Day 3: Custom helper functions (module)    |
| `day3_main.py`  | Day 3: Testing modules and error handling  |
| `hello.txt`     | File created/written by Python             |
| `day4_oop.py`   | Day 4: Classes, objects, and inheritance   |

---

## ✅ What I’ve Learned

### 🧠 Day 1: List Comprehensions
- Fast and readable way to create lists
- Used filtering and conditions
- Example:
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
- Example:
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
- Example:
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

## 🚀 Next Steps
- Day 5: Practice file reading/writing with CSV and JSON
- Start building mini-projects using Python

---

## 📌 Repo Info
- Author: [poohsted](https://github.com/poohsted)
- Started: June 2025
