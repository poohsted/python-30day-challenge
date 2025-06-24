# day12_numpy.py - Part 1: Broadcasting

import numpy as np

print("--- NumPy Broadcasting ---")

# Example 1: Adding a scalar to an array
arr = np.array([1, 2, 3, 4])
scalar = 10
result_scalar_add = arr + scalar
print(f"Array: {arr}")
print(f"Scalar added: {result_scalar_add}") # Each element gets 10 added

print("\n")

# Example 2: Adding a 1D array to a 2D array (broadcasting rows)
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])
row_vector = np.array([1, 2, 3])
# row_vector (shape (3,)) is broadcasted across each row of matrix (shape (2,3))
result_row_add = matrix + row_vector
print(f"Matrix:\n{matrix}")
print(f"Row Vector: {row_vector}")
print(f"Matrix + Row Vector:\n{result_row_add}")

print("\n")

# Example 3: Adding a 1D column vector (requires reshaping)
# To broadcast across columns, the 1D array needs to be a column vector (shape (rows, 1))
col_vector = np.array([[100],
                       [200]]) # Shape (2,1)
# col_vector (shape (2,1)) is broadcasted across each column of matrix (shape (2,3))
result_col_add = matrix + col_vector
print(f"Matrix:\n{matrix}")
print(f"Column Vector:\n{col_vector}")
print(f"Matrix + Column Vector:\n{result_col_add}")

print("\n--- End Broadcasting ---\n")