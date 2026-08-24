'''
.ravel() method returns a flattened one-dimensional array, but it returns a view of the original array whenever possible.
This means that if you modify the returned array, it may also modify the original array.

.ravel() -> view
.flatten() -> copy

Flattening is the process of converting a multi-dimensional array into a one-dimensional array.
In NumPy, you can flatten an array using the `flatten()` method or the `ravel()` function.
'''
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Using flatten() method
flat_arr = arr.flatten()
print("Flattened array using flatten():", flat_arr)  # prints [1 2 3 4 5 6 7 8 9]

# Using ravel() function
raveled_arr = arr.ravel()
print("Flattened array using ravel():", raveled_arr)  # prints [1 2 3 4 5 6 7 8 9]
raveled_arr[0] = 10  # Modifying the raveled array
print("Modified original array:", arr)  # prints  [[10  2  3] [ 4  5  6] [ 7  8  9]]