'''
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
'''

number = int(input('Введите число n:'))
n = str(number)
n1 = n + n
n2 = n + n + n
total = int(n) + int(n1) + int(n2)
print('the sum is = ', total)