# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [1, 1, 2, 3, 3, 4, 5, 2, 6]
resultList = []
for i in list:
    if list.count(i) == 1:
        resultList.append(i)
print(resultList)
