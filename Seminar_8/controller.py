import view as v
import form_lists as fl
import output_date as od
import input_date as id


def Butt():
    names = id.InitName()
    marks = id.InitMark
    subs = id.InitSub()
    v.Menu()
    a = input('Введите номер функции: ')
    if a == "1":
        z = od.AddName(names)
        kl = fl.AddDictSubAndMark(subs)
        kll = fl.AddDictNameAndSubAndMark(kl,z)
        od.FileAdd(kll)
        print(kll)
    elif a == '2':
        sad = od.AddSub(subs)
        kl = fl.AddDictSubAndMark(sad)
        kll = fl.AddDictNameAndSubAndMark(kl,names)
        print(kll)
    elif a == '3':
        kl = fl.AddDictSubAndMark(subs)
        sax = od.AddMark(kl,names)
        print(sax)
    elif a == '4':
        v.ViewName(names)
    elif a == '5':
        kl = fl.AddDictSubAndMark(subs)
        kll = fl.AddDictNameAndSubAndMark(kl,names)
        v.ViewMarkStudent(kll,names)
    elif a == '6':
        names = id.RandomName(10)
        subs = id.RandomSub()
        kl = fl.AddDictSubAndMarkRandom(subs)
        kll = fl.AddDictNameAndSubAndMark(kl,names)
        od.FileAdd(kll)
    elif a == '7':
        kl = fl.AddDictSubAndMark(subs)
        kll = fl.AddDictNameAndSubAndMark(kl,names)
        od.FileAdd(kll)
    elif a == '8':
        file = od.ImportFromFile()
        av = od.Average(file)
        print(f'Средний балл: {av}')
    elif a == '9':
        Exception()
