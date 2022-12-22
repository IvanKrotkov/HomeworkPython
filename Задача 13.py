#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
list  = [1.1, 1.2, 3.1, 5, 10.01]
list1 = []
for i in range(0,len(list)):
    if list[i]-int(list[i]) == 0:
        continue
    list1.append(round(list[i]-int(list[i]),2))
result = max(list1) - min(list1)
print(result)

