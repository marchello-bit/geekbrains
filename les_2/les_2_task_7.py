#Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
#https://drive.google.com/file/d/1rMFGA4gKeUYoIXjR8GYV-ttVT4-hQJMv/view?usp=sharing
n=int(input('Введите n-натуральное число:'))
for i in range(n):
    an=1+1*(n-1)
    Sn=((1+an)/2)*n
    print(Sn)
    Snp=n*(n+1)/2
    print(Snp)
    if Sn == Snp:
        print('Теорема доказана')
        break


