#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
n = int(input('Введите натуральное число число:'))
chet=0
ne_chet=0
while n > 0:
    a = n % 10
    if a==0 or a==2 or a==4 or a==6 or a==8:
        chet=chet+1
    else:
        ne_chet=ne_chet+1
    
    n = n//10
print('Количество четных чисел:', chet)
print('Количество нечетных чисел:', ne_chet)
