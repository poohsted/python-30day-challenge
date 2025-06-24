# Part 2: Universal Functions (Ufuncs)

import numpy as np

print("--- NumPy Universal Functions (Ufuncs) ---")

data = np.array([-1.5, 0.0, 2.7, -3.1, 4.0])
print(f"Original data: {data}")

# Apple various ufuncs
print(f"Absolute values: {np.abs(data)}")
print(f"Square root (only positive elements): {np.sqrt(np.maximum(0,data))}")
print(f"Exponential: {np.abs(data)}")
print(f"Sine: {np.sin(data)}")
print(f"Ceiling (round up): {np.ceil(data)}")
print(f"Floor (round down): {np.floor(data)}")
print(f"Rounded to nearest integer: {np.round(data)}")

# Ufuncs can also take multiple arrays
arr1 = np.array([1, 5, 2, 8])
arr2 = np.array([3, 2, 6, 4])
print(f"\nArray 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Element-wise maximum: {np.maximum(arr1, arr2)}")
print(f"Element-wise maximum: {np.minimum(arr1, arr2)}")

print(f"\n--- End Ufuncs --\n")