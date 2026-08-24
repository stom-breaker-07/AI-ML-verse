'''
used to concat to arrays in numpy
syntax like this
numpy.concatenate((a1, a2, ...), axis=0)

axis 0 -> concatenate along rows (vertical stacking)
axis 1 -> concatenate along columns (horizontal stacking)

remember you are passing arrays in tuples and the axis is optional, 
if not provided it will concatenate along the first axis (axis=0).
'''
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

concatenated_arr = np.concatenate((arr1[::], arr2[::-1]), axis=1)
print(concatenated_arr) 