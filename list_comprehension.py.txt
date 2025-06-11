"""
list_comprehension.py
Practice file for Day 1 of 30-Day Intermediate Python Challenge.
Demonstrates list comprehensions in various forms.
"""

# Example 1: Square numbers from 0 to 9
squares = [i**2 for i in range(10)]
print("Squares:", squares)

# Example 2: Filter even numbers
numbers = list(range(1, 11))
even = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even)

# Example 3: Multiplication table (flattened)
table = [i * j for i in range(1, 4) for j in range(1, 4)]
print("Multiplication Table:", table)
