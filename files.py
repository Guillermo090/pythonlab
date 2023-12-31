file = open('./text.txt')

print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())


for line in file:
    print(line)

file.close()

with open('./text.txt', 'r') as file:
    for line in file:
        print(line)

# para escribir al final del archivo
with open('./text2.txt', 'r+') as file2:
    for line in file2:
        print(line)
    file2.write('\nnuevas cosas en este archivo')


# para reemplazar el texto del archivo
with open('./text3.txt', 'w+') as file3:
    for line in file3:
        print(line)
    file3.write('\nnuevas cosas en este archivo')
