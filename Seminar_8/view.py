def Menu():
    print('Выберите функцию: \
        \n 1.Добавление нового студента \
        \n 2.Добавление предмета \
        \n 3.Добавление оценки ученику по предмету\
        \n 4.Показ списка учеников \
        \n 5.Показ листа оценок конкретного ученика\
        \n 6.Выход из программы')


def ViewName(nameLists):
    for i in nameLists:
        print(i)

def ViewMarkStudent(dictic,nameList):
    a = input(f"Введите имя и Фамилию ученика {nameList}: ")
    for k,v in dictic.items():
        if k == a:
            print(v)



