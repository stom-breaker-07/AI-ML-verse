'''
insert() function in NumPy is used to insert values into an array at specified indices. It returns a new array with the values inserted, without modifying the original array.
The syntax for the insert() function is as follows:
numpy.insert(arr, indices, values, axis=None)
'''
import numpy as np

arr=np.array([[1,2],[3,4],[5,6]])
print(arr)

inserted_arr = np.insert(arr, 1, [7,8], axis=0)
print(inserted_arr)  # prints [[1 2]
                     #         [7 8]
                     #         [3 4]
                     #         [5 6]]

inserted_arr_col = np.insert(arr, 2, [7,8,9], axis=1)
print(inserted_arr_col)  # prints [[1 7 2]
                     #         [3 8 4]
                     #         [5 9 6]]