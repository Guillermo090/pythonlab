
# funciones lambda

def increment(x):
    return x + 1

result = increment(10)
print(result)

# lo mismo con lambda

increment_lambda =  lambda x : x + 1 
print(increment_lambda(20))


# otro lambda
full_name = lambda first_name, last_name : f'Nombre completo es {first_name.title()} {last_name.title()}'

print( full_name('Guillermo','Royo') )


# funciones high order function HOF

def high_ord_func(x, func):
    return x + func(x)

#  solo envio funcion increment no se ejecuta, por eso se envia sin parentesis
result = high_ord_func(2,increment)
print(result)


# una hof lambda
high_ord_func_v2 = lambda x, func: x + func(x)

final_hof_lambda = high_ord_func_v2(2, increment_lambda)
print(final_hof_lambda)