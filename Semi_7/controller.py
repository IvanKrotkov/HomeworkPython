import import_date as id
import output_date as od


def Butt():
    fal = input('Выберите режим: 1 - ввод данных, 2 - вывод данных: ')
    if fal == '1':
        a = id.Init()
        fall = input('Отсортировать данные по id?(Да/Нет): ')
        if fall == 'Да' or fall == 'да':
            od.SaveDate(a)
            od.SortingFile()
        else:
            od.SaveDate(a)
            z = input("Показать данные?(да/нет): ")
            if z == 'Да' or z == 'да':
                od.ViewDate()
    if fal == '2':
        e = input('Отсортировать данные по id?(Да/Нет): ')
        if e == 'Да' or e == 'да':
            od.SortingFile()
        else:
            od.ViewDate()
