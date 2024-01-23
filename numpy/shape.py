import numpy as np

# definimos un array random de 3 x 2
arr = np.random.randint(1,10,(3,2))
print(arr)

print(arr.shape)

print(arr.reshape(1,6))
print(arr.reshape(2,3))

print(f'Ordenado en C :\n {np.reshape(arr,(2,3),"C")}')
print(f'Ordenado en base a mi local : \n {np.reshape(arr,(2,3),"A")}')
print(f'Ordenado en Fortran :\n {np.reshape(arr,(2,3),"F")}')