#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt','r') as dataOne:
    k = dataOne.read()
with open('file2.txt','r') as dataTwo:
    a = dataTwo.read()
splitOne = k.split()
splitTwo = a.split()
listResult = []
res =''
for i in range(len(splitOne)):
    if i == 0 or i == 4 or i == 8:
        summ = str(int(splitOne[i]) + int(splitTwo[i]))
        listResult.append(summ)
    else:
        listResult.append(splitOne[i])
for i in listResult:
    res = res + i
with open('fileResult.txt','w') as dataResult:
    dataResult.write(f'{res}')
