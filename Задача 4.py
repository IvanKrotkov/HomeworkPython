# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой
# четверти (x и y).

numberQuarter = int(input("Введите номер четверти: "))
if numberQuarter > 4:
    print("Такого номера четверти нет")
elif numberQuarter == 1:
    print("x = [0,+infinity), y = [0,+infinity)")
elif numberQuarter == 2:
    print("x = (-infinity,0], y = [0,+infinity)")
elif numberQuarter == 3:
    print("x = (-infinity,0], y = (-infinity,0]")
elif numberQuarter == 4:
    print("x = [0,+infinity), y = (-infinity,0]")
