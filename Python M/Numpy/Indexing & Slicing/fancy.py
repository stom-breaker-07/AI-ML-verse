# Fancy indexing is a powerful feature in NumPy that allows you to select elements from an array using arrays of indices. 
# This can be useful for selecting specific rows or columns, or for creating new arrays based on existing ones.
import numpy as np

arr=np.array([10,20,30,40,50])

print(arr[[0,2,4]])  # prints [10 30 50]