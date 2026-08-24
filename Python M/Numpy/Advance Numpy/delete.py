# delete(arr, index,axis)

import numpy as np

arr=np.array([1,2,3,4,5,6])
print(arr)

new_arr = np.delete(arr,2)

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)

new_arr_2d= np.delete(arr_2d,1,0)
print(new_arr_2d)

new_arr_2d_col= np.delete(arr_2d,1,1)
print(new_arr_2d_col)