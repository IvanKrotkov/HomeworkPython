import input_date as id
import form_lists as fl


def AddMark(a,names):
    sina = a
    ssim = fl.AddDictNameAndSubAndMark(a,names)  
    sds = input(f"Введите имя и фамилилю ученика {names}: ")
    asa = [i for i in sina.keys()]
    for key,value in ssim.items():
        if key == sds:
            a = input(f"Введите предмет для оценки {asa}: ")
            for k,v in sina.items():
                if k == a:        
                    sinas = [h for h in v]
                    sinas.append(input("Введите оценку: "))
                    c = {k:sinas}
                    sina.update(c)
                    break
            ss = {key: sina}
            ssim.update(ss)
    return ssim

def AddName(names):
    sina = names
    sina.append(input('Введите имя и фамилию: '))
    return sina

def AddSub(zsss):
    zs = zsss
    zs.append(input("Введите предмет: "))
    return zs

def FileAdd(dictea):
    with open('Seminar_8\save.txt','w') as file:
        for k,v in dictea.items():
            for z,d in v.items():
                file.write(f'{k} - {z}: {d} \n')

def ImportFromFile():
    with open('Seminar_8\save.txt','r') as file:
        z = file.read()
        f = z.split()
    return f
def Average(file):
    subs = [file[i] for i in range(2,len(file),4)]
    subs_s= set(subs)
    res = []
    print(subs_s)
    a = input(f'Введите предмет {subs_s} : ')
    for i in range(2,len(file)-1,4):
        if a in file[i]:
            for j in range(0,len(file[i+1])):
                if file[i+1][j].isdigit():
                    res.append(file[i+1][j])
    res = list(map(int,res))
    result = 0
    for i in res:
        result += i
    result = result/len(res)
    return result