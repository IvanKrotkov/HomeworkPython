# Реализуйте алгоритм перемешивания списка.

list = [1, 2, 3, 4, 5]
for i in range(0,len(list)):
    for j in range(0,int(len(list)/2)):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
print(list)