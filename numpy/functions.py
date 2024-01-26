import numpy as np

arr = np.random.randint(1,20,10)
print(arr)

matriz = arr.reshape(2,5)
print(matriz)

# devuelve el max del arreglo
print( arr.max() )
# devuelve el max de matriz en base al eje 0
print( matriz.max(0) )

# devuelve el indice q contiene el max en eje 0
print( arr.argmax(0) )
# devuelve el indice q contiene el max en eje 0
print( matriz.argmax(1) )

print( arr.min() )
print( matriz.min(0) )


# devuelve el indice q contiene el max en eje 0
print( arr.argmin() )
# devuelve el indice q contiene el max en eje 0
print( matriz.argmin(1) )


print(arr)
print(arr.ptp())
print(matriz )
print(matriz.ptp(0))
print(matriz.ptp(1))

print( arr )
print( np.percentile(arr, 50) )

# mediana -> percentil 50
print( np.median(arr) )


print( np.median(matriz,1) )

# desviación standard
print( np.std(arr) )

# varianza
print( np.var(arr) )

# media -> suma de todos los valores dividido por la cantidad de valores
print( np.mean(arr) )

a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[5,6]])
print(b)
print( np.concatenate((a,b),axis=0) ) 

# transpuesta de una matriz
print( b.T ) 