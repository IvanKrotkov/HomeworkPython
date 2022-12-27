# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число: "))
list = []
sqrt = str(n**0.5)
ss = sqrt.split('.')
if ss[1] == '0':
    for i in range(1,3):
        list.append(sqrt)
        n = int(n**0.5)
else:
    for i in [2, 3, 5, 7]:
        while n > i:
            if n % i == 0:
                list.append(i)
                n = n/i
            elif n % i in [2,3,5,7] != 0:
                if n in list:
                    break
                list.append(int(n))
                break
            else:
                break


print(list)
