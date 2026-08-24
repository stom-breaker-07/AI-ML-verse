# sliceing in numpy array

import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr[0:2,1:3])  # prints [[2 3]
print(arr[:2,:3])  # prints [[1 2 3]
                   #         [5 6 7]]
print(arr[::-1,::-1])