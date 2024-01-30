import numpy as np

arr = np.arange(0,11)
print(arr)

trozo_arr = arr[0:6]
print(trozo_arr)

trozo_arr[:] = 0
print(trozo_arr)
print(arr)

arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
print(arr)