import input_date as id
import form_lists as fl


def AddMark(a,names):
    sina = a
    ssim = fl.AddDictNameAndSubAndMark(a,names)            #fl.AddDictSubAndMark()
    sds = input(f"Введите имя и фамилилю ученика {names}: ")
    asa = [i for i in sina.keys()]
    # print(sina)
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
