#Вычислить число c заданной точностью d

#Пример:

#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

a = int(input('Введите точность(кол-во цифр после запятой): '))
c = math.pi
c1 = round(c,a)
print(c1)