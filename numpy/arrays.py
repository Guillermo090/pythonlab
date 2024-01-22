import numpy as np

python_list = list(range(0,10))
print(python_list)

numpy_array = np.arange(0,10)
print(numpy_array)

numpy_array_2 = np.arange(0,20,2)
print(numpy_array_2)

zeros = np.zeros(3)
print(zeros)

zeros_2 = np.zeros((10,10))
print(zeros_2)

ones = np.ones((10,10))
print(ones)

linspace = np.linspace(0,10,100)
print(linspace)

eye = np.eye(4)
print(eye)

rand = np.random.rand(4,4)
print(rand)


randint = np.random.randint(1,1000,(5,5))
print(randint)