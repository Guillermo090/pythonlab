for i in range(1,11):
    print(i)

my_iter = iter(range(1,11))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Un iterable se define como el objeto que contiene un número contable 
# con valores y este al tener un valor puede recorrer uno a uno los 
# elementos que la contienen como una estructura de datos y operar con ellos, 
# pero a la vez se rigen bajo la instrucción que se le es dada, 
# con lo cual son dependientes de la instrucción a recibir.

# Los metodos de su uso son dos __iter__() y __next__() .