import numpy as np

# define with base type
arr = np.array([1,2,3,4])
print( f'arreglo en numpy es {arr}' )
print( f'tipo de arreglo creado por defecto es {arr.dtype}' )

# define with dtype parameter
arr = np.array([1,2,3,4], dtype='float64')
print( f'tipo de arreglo creado con dtype especifico es : {arr.dtype}' )

# redefine with astype method
arr = arr.astype(np.float32)
print( f'tipo de arreglo modificado por astype es {arr.dtype}' )

# 
arr = np.array([0,1,2,3,4])
print( f'arreglo definido en numpy es  : {arr}' )
arr = arr.astype(np.bool_)
print( f'arreglo modificado por astype definido como booleano es : {arr}' )
print( f'tipo de arreglo modificado por astype definido como booleano es : {arr.dtype}' )


# redefine list of strings to int8
arr = np.array(['0','1','2','3','4'])
print( f'arreglo definido en numpy es  : {arr}' )
arr = arr.astype(np.int8)
print( f'tipo de arreglo modificado por astype : {arr.dtype}' )

# all data must be the same data type
print('todos los datos de un arreglo deben tener el mismo tipo de dato')

