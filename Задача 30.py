# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
a = int(input("Введите первый элемент последовательности: "))
b = int(input("Введите разность между текущим и предыдущем элементом: "))
c = int(input("Введите количество элементов прогрессии: "))

ll = [i for i in range(a,a+c*b,b)]
print(ll)


