#Определить, является ли год, который ввел пользователь, високосным или не високосным.
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
N = int(input('Введите год N:'))

if N%4==0 and N%100!=0 or N%400==0:
  print('Год високосный')
else:
  print('Год не високосный')
