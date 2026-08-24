'''
Reshaping in array is a powerful feature in NumPy that allows you to change the shape of an array without changing its data.
This can be useful for various applications, 
such as preparing data for machine learning models or visualizing data in different formats.

'''
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
  # reshapes the array into a 3x3 matrix
print(arr.reshape(3,3)) # so it is void of changing the data but only the shape of the array is changed 
print(arr)