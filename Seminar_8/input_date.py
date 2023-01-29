import random
def InitName():
    nameS = ['Ivan Kor','Danil Kri']
    return nameS
def InitSub():
    subjects = ['Math','Bio']
    return subjects

def InitMark(f = False):
    marks = []
    if f:
        marks.append(input('Введите оценку: '))
    return marks


    
def RandomName(n):
    sa = ['Ivan','Maksim','Danil','Kirill','Sergey','Andrey','Dima']
    nameS = [random.choice(sa) for i in range(0,n)]
    sss = ['Smirnov','Ivanov','Popov','Petrov','Avilin','Abramov','Kuznetsov']
    surNameS = [random.choice(sss) for i in range(0,n)]
    res = list(zip(nameS,surNameS))
    return res

def RandomSub():
    sa = ['Chemystry','Biology','Math','Socialogy','Literature','Physics']
    bon = [random.choice(sa) for i in range(0,5)]
    return bon

def RandomMarks():
    sa = [random.randint(2,5) for i in range(0,1)]
    return sa