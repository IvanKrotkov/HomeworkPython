#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [1 , 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("Введите число: "))
count = 1
array = []
for i in range(1,num+1):
    count = count*i
    array.insert(i,count)
    
print(array)

     