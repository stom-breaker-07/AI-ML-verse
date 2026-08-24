# to change the data type of the array
import numpy as np

np_arr=np.array([[1.2,2],[3.5,4]])
print("Data type of array",np_arr.dtype)

int_arr=np_arr.astype('int32')
print("Data type of array",int_arr.dtype)