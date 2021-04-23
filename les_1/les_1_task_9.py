#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
print('Введите три разных числа')
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))

if (a<b and a>c) or (a<c and a>b):
   print("а - среднее число:")
elif (b<a and b>c) or (b<c and b>a):
   print("b-среднее число")
else:
   print("c-среднее число")
