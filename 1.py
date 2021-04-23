print('Введите три разных числа')
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))
sr=float((a+b+c)/3)
print(sr)
if abs(sr-a) < abs(sr-b):
  print('Среднее число а:' a)
else:
  print('Среднее число c:' c)
