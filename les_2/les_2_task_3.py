#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
n = int(input('Введите число:'))
p=0
while n > 0:
    a = n % 10
    p = p*10 + a 
    n = n//10
print('Число в обратном порядкке:', p)
