# Напишите программу, которая принимает на вход
#  координаты двух точек и находит расстояние между ними в
# 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты первой точки: ')
x1 = int(input("х1: "))
y1 = int(input("у1: "))
print('Введите координаты второй точки: ')
x2 = int(input("х2: "))
y2 = int(input("у2: "))


def Range(x1, x2, y1, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    print(distance)



Range(x1, x2, y1, y2)
