#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
N = int(input('Введите трезначное число:'))
a=N//100
b=N//10-a*10
c=N-a*100-b*10
s=a+b+c
p=a*b*c
print(s)
print(p)
