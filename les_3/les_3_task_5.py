#В массиве найти максимальный отрицательный элемент.
#Вывести на экран его значение и позицию в массиве.
#Не путайте «минимальный» и «максимальный отрицательный»!


import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]

for i in range(SIZE):
    if array[i] < 0:
        if max_ <= array[i]:
            max_ = array[i]
            a = i
print('Позиция в массиве:', a)  
print('Значение:', max_)

        
