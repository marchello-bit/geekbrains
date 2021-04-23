#По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
print('Введите координаты двух точек')

x1 = int(input('Введите x1:'))
y1 = int(input('Введите y1:'))
x2 = int(input('Введите x2:'))
y2 = int(input('Введите y2:'))
k=((y1-y2)/x1)/(1-x2/x1)
b=y2-x2*k
print('y=',k,'*x +',b)




