# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
line = '111112222334445'

def Compression(string):
    sa = ''
    res = ''
    count = 0
    for i in string:
        if i != sa:
            if count>0:
                res += str(count) + sa
            count = 1
            sa = i
        else:
            count +=1 
    res+=str(count) + sa
    return res
def Recovery(string):
    dist = ''
    for i in string:
        if not i.isdigit():
            return RecoverySec(string)
    for i in range(0,len(string)-1,2):
        dist = dist + int(string[i])*string[i+1]
    return dist
def RecoverySec(string):
    dist = ''
    se = ''
    for i in string:
        if i.isdigit():
            se += i
        else:
            dist += int(se) * i
            se = ''
    return dist
a = Compression(line)
b = Recovery(a)
print(a)
print(b)
