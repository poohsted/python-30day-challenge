# Part 4: Array Manipulation

import numpy as np

print("--- NumPy Array Manipulation ---")

# Reshaping
arr_1d = np.arange(1, 13) # Creates array [1, 2, ..., 12]
print(f"Original 1D array: {arr_1d}")
matrix_3x4 = arr_1d.reshape(3, 4)
print(f"Reshape to 3x4 matrix:\n{matrix_3x4}")

matrix_4x3 = arr_1d.reshape(4, 3)
print(f"Reshaped to 4x3 matrix:\n{matrix_4x3}")

# Concatenating
arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])
print(f"\nArray A:\n{arr_a}")
print(f"Array B:\n{arr_b}")

# Horizontal stack (column-wise)
h_stack = np.hstack((arr_a, arr_b))
print(f"Horizontal Stack (np.hstack):\n{h_stack}")

# Vertical stack (row-wise)
v_stack = np.vstack((arr_a, arr_b))
print(f"Vertical Stack (np.vstack):\n{v_stack}")

# Generic concatenate (can do both with 'axis' parameter)
concat_axis0 = np.concatenate((arr_a, arr_b), axis=0) # Same as vstack
concat_axis1 = np.concatenate((arr_a, arr_b), axis=1) # Same as hstack
print(f"Concanate (axis=0):\n{concat_axis0}")
print(f"Concatenate (axis=1):\n{concat_axis1}")

# Splitting
data_to_split = np.arange(16).reshape(4, 4)
print(f"\nData to Split:\n{data_to_split}")

# Split into two equal rows
split_rows = np.split(data_to_split, 2, axis=0)
print(f"Split into 2 rows:\n{split_rows[0]}\n---\n{split_rows[1]}")

# Split into four equal columns
split_cols = np.split (data_to_split, 4, axis=1)
print(f"Split into 4 columns (first column:\n{split_cols[0]})")

print("\n--- End Array Manipulation ---\n")