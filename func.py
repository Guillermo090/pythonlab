
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