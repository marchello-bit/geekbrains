#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
n=int(input('Введите n - количество элементов ряда:'))

for i in range(n):
    a=1*(1-(pow(-0.5,n)))/(1-(-0.5))
 
print(a)

