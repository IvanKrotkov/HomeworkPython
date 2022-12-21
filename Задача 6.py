# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
num = input("Введите число: ")


def FloatSum(num):
    line = num.split(".")
    summ = 0
    for i in range(0, len(line)):
        for j in range(0, len(line[i])):
            summ = summ + int(line[i][j])
    return summ

def SumDigit(num):
    g = 0
    for i in range(0, len(num)):
        g = g + int(num[i])
    return g


def SearchDot(num):
    if num.count('.') == 1:
        return True
    else:
        return False


if SearchDot(num):
    print(FloatSum(num))
else:
    print(SumDigit(num))
