# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int(input('Введите степень: '))
def RandomDigit():
    randomK = random.randint(0, 100)
    return randomK
result = ''
for i in range(k, -1,-1):
    if i == 0:
        result = result + f'{k} = 0'
    elif i == 1:
        result = result + f'{RandomDigit()}x + '
    else:
        result = result + f'{RandomDigit()}x**{i} + '
with open('answer.txt','w') as data:
    data.write(f'{result}')



