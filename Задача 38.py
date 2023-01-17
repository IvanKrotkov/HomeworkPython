#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line = 'фыв тут ыы абвыфв бдж фыыв абвыю абв'
lists = line.split()
print(lists)
res = ''
s = list(filter(lambda line: 'абв' not in line,lists))
for i in s:
    res = res + i + ' '

print(res)