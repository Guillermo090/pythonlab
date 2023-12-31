numbers = [1,2,3,4]

numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)
print(numbers_v2)

# map con iteracion de lista
numbers_v3 = list(map(lambda i:i*2, numbers))
print(numbers_v3)


# map con entrada de varias listas
print("--------------")
numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]
print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)

# map con entrada de diccionarios
print("----------------------")
print("map con diccionarios")
items= [
    {
        "product": "camisa",
        "price": 100,
    },
    {
        "product": "pantalon",
        "price": 300
    },
    {
        "product": "gorro",
        "price": 200
    }
]

# map modifica estado original, no crea uno nuevo
prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
    item['taxes'] = item["price"] * .19
    return item

new_items = list(map(add_taxes, items))
print(items)
print(new_items)