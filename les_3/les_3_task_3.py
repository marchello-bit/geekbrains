#В массиве случайных целых чисел поменять местами
#минимальный и максимальный элементы.


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]
min_ = array[0]

for i in range(SIZE): 
    if max_ <= array[i]:
        max_ = array[i]
    if min_ >= array[i]:
        min_ = array[i]
for i in range(SIZE): 
    if max_ == array[i]:
        array.pop(i)
        array.insert(i,min_)
    elif min_ == array[i]:
        array.pop(i)
        array.insert(i,max_)
print('Минимальное значение массива: ', min_)
print('Максимальное значение массива: ', max_)
print('Получившийся массив:', array)
        

    
