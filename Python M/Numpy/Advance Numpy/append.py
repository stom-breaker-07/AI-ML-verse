'''
appending a values to numpy array
'''

import numpy as np

arr = np.array([1, 2, 3])
print(arr)

appended_arr = np.append(arr, [4, 5])
print(appended_arr)  # prints [1 2 3 4 5]