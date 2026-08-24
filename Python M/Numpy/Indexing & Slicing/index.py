# it tells about the indexing in numpy array
import numpy as np
 
np_arr=np.array([[1,2],[3,4],[5,6]])
print(np_arr[0,0])  # prints 1
print(np_arr[1,1])  # prints 4
print(np_arr[2,0])  # prints 5
print(np_arr[0])  # prints [1 2]   
print(np_arr[-1,-1])