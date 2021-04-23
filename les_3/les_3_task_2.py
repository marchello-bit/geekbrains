#Во втором массиве сохранить индексы четных элементов первого массива.
#Первый массив заполнить случайными числами.
#Индексация начинается с нуля!


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
print(array)
even = []
for i in range(SIZE):
    if array[i] % 2 == 0:
        even.append(i)
print('Массив с индексами четных элементов:', even)
