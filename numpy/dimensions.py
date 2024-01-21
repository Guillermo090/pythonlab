import numpy as np

# scalar -> cero dimensions
scalar = np.array(42)
print(scalar)
print(f'scalar tiene {scalar.ndim} dimensiones')

# vector -> one dimension
vector = np.array([1,2,3])
print(vector)
print(f'vector tiene {vector.ndim} dimensiones')

# matriz -> two dimensions
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(f'matriz tiene {matriz.ndim} dimensiones')

# tensor -> three or more dimentions
tensor = np.array([[[1,2,3],[4,5,6],[4,5,6],[4,5,6]],[[1,2,3],[4,5,6],[4,5,6],[4,5,6]]])
print(tensor)
print(f'tensor tiene {tensor.ndim} dimensiones')

# define number of dimensions at definition
vector = np.array([1,2,3], ndmin=10)
print(vector)
print(vector.ndim)

# add or remove dimensions
expand = np.expand_dims(np.array([1,2,3]),axis=1)
print(expand)
print(expand.ndim)

# 
print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)

