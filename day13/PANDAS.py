import pandas as pd
import numpy as np

print("--- Pandas Series ---")

# 1. Creating a Series from a List
s1 = pd.Series([10, 20, 30, 40, 50])
print("Series from list:\n", s1)

print("\n")

# 2. Creating a Series with custom index
s2 = pd.Series([10, 20, 30, 40], index = ['a', 'b', 'c', 'd'])
print("Series from NumPy array with custon index:\n", s2)

print("\n")

# 3. Creating a Series from a NumPy array
np_array = np.array([100, 200, 300])
s3 = pd.Series(np_array)
print("Series from NumPy array:\n", s3)

print("\n")

# 4. Creating a Series from a Dictionary
# Dictionaries keys become the index, values become the data.
data_dict = {'apple': 1.5, 'banana': 0.75, 'orange': 2.0}
s4 = pd.Series(data_dict)
print("Series from distionary:\n", s4)

print("\n")

# 5. Accessing elements in a Series
print("Accessing elements:")
print("First element:", s1[0])  # Access by index
print("Element with index 'c':", s2['c'])  # Access by custom index
print("Elements from index 1 to 3:", s1[1:4])  # Slicing
print("Elements with index 'a' to 'c':", s2['a':'c'])  # Slicing with custom index
print("\n")

# 6. Modifying elements in a Series
s1[0] = 100  # Modify by index
print("Modified Series s1:\n", s1)
s2['b'] = 50  # Modify by custom index
print("Modified Series s2:\n", s2)
print("\n")

# 7. Performing operations on Series
s5 = s1 + s2  # Element-wise addition
print("Element-wise addition of s1 and s2:\n", s5)
s6 = s1 * 2  # Element-wise multiplication
print("Element-wise multiplication of s1 by 2:\n", s6)
print("\n")