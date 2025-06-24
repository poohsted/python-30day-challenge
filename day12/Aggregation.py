# Part 3: Aggregation with Axis

import numpy as np

print("--- Numpy Aggregation with Axis ---")

matrix_2d = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print(f"Original 2D Matrix:\n{matrix_2d}")

# Sum of all elements
print(f"\nSum of all elements: {np.sum(matrix_2d)}")

# Sum along rows (axis=1) - sums elements within each row
print(f"Sum along rows (axis=1): {np.sum(matrix_2d, axis=1)}")

# Sum along columns(axis=0) - sums elements within each column
print(f"Sum along columns (axis=0): {np.sum(matrix_2d, axis=0)}")

# Mean (average)
print(f"\nMean of all elements: {np.mean(matrix_2d):.2f}")
print(f"Mean along rows (axis=1): {np.mean(matrix_2d, axis=1)}")
print(f"Mean along columns (axis=0): {np.mean(matrix_2d, axis=0)}")

# Min/Max
print(f"\nMinimum of all elements: {np.min(matrix_2d)}")
print(f"Maximum along rows (axis=1): {np.max(matrix_2d, axis=1)}")
print(f"Minimum along columns (axis=0): {np.min(matrix_2d, axis=0)}")

print("\n--- End Aggregation ---\n")