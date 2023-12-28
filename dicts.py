

person = {
    'name': 'Guillermo',
    'last_name': 'Royo',
    'langs': ['Python','Javascript','C#'],
    'age' : 23,
    'dev-level': 'Senior'
}
print(person)


# eliminar elemento de la lista
del person['last_name']
print(person)


print((8 / 2) + 4 * 8)



# DICT COMPREHENSION
import random
countries = ['col','mex','bol','pe']

population_v2 = { 
                    country: random.randint(1,100)
                    for country in countries
                }
print(population_v2)

# se puede dividir un list comprehension en llave valor cuando se les da un dict iterado de entrada
result = {country:population for (country,population) in population_v2.items() if population > 20}
print(result)


text = 'Hola, soy Nicolas'

unique = { c:c.upper() for c in text if c in 'aeiou' }
print(unique)