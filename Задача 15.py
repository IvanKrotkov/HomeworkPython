# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input())


def Fib(n):

    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return Fib(n+2)-Fib(n+1)
    else:
        return Fib(n-1)+Fib(n-2)


list = []
for i in range(-num, num+1):
    list.append(Fib(i))
print(list)
