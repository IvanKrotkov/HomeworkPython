#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input("Введите кол-во элементов: "))
list = [i for i in range(-num,num+1)]
print(list)
with open('file.txt','r') as data:
    result = 1
    for line in data:
        result = result*list[int(line)]
print(result)

    