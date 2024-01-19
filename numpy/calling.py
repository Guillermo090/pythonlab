import numpy as np

# define with base type
arr = np.array([1,2,3,4])
print( arr.dtype )

# define with dtype parameter
arr = np.array([1,2,3,4], dtype='float64')
print( arr.dtype )

# redefine with astype method
arr = arr.astype(np.float32)
print( arr.dtype )

# 
arr = np.array([0,1,2,3,4])
arr = arr.astype(np.bool_)
print( arr.dtype )

# redefine list of strings to int8
arr = np.array(['0','1','2','3','4'])
arr = arr.astype(np.int8)
print( arr.dtype )

# all data must be the same data type

