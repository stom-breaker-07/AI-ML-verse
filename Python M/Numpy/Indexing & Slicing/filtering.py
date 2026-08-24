# Boolean Masking is a powerful feature in NumPy that allows you to filter elements of an array based on a condition. It creates a boolean array (mask) where each element indicates whether the corresponding element in the original array satisfies the condition.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr[arr>5])  # prints [ 6  7  8  9 10]