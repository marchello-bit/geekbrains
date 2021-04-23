#В одномерном массиве найти сумму элементов,
#находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.


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
        a = i
    if min_ >= array[i]:
        min_ = array[i]
        b = i
for i in range(SIZE):
    if a <= b:
        S = array[a+1:b]
    else:
        S = array[b+1:a]
n = len(S)
sum_ = 0
for i in range(n):
    sum_ += S[i]
print('Позиция минимального элемента:', b,'Значение минимального элемента:', min_)
print('Позиция максимального элемента:', a, 'Позиция максимального элемента:', max_)
print('Полученный массив:',S) 
print('Сумма элементов массива:',sum_)
       


