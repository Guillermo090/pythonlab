
numbers = [ num for num in range(1,10)]
print(numbers)

# agregar al final
numbers.append(700)
print(numbers)

#insertar en indice especifico
numbers.insert(0,'insertado en 0')
print(numbers)
numbers.insert(3,'insertado en 3')
print(numbers)

# detectar indice
index = numbers.index(4)
print(index)

# eliminar elemento
numbers.remove('insertado en 3')
print(numbers)

# eliminar por indice
numbers.pop(0)
print(numbers)

# revertir orden de arreglo
numbers.reverse()
print(numbers)
 
# ordenar arreglo numeros o por orden alfabetico pero no tipos de datos mezclados
numbers.sort()
print(numbers)
