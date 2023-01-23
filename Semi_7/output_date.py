

def SaveDate(list):
    with open('Semi_7\spravochnick.txt', 'a') as file:
        for i in list:
            file.write(f'{i} ')
        file.write('\n')


def ViewDate():
    global z
    global f
    z = False
    f = False
    y1 = input("Желаете увидеть только имя и фамилию?(да/нет): ")
    bas = input(
        'Вы хотите увидеть все записи или какую то конретную(все/конкретную): ')
    if bas == "Все" or bas == 'все':
        with open('Semi_7\spravochnick.txt', 'r') as file:
            a = file.readlines()
            if y1 == 'да' or y1 == 'Да':
                count = 0
                for i in a:
                    for j in range(0, len(i)):
                        if i[j].isdigit():
                            continue
                        else:
                            print(i[j], end='')
                            if i[j] == ' ':
                                count = count + 1
                            if count >= 3:
                                count = 0
                                break
            else:
                for i in a:
                    print(i)
    else:
        y = input("Выберите критерий вывода: 1 - имя,фамилия; 2 - id: ")
        if y == '2':
            with open('Semi_7\spravochnick.txt', 'r') as file:
                a = file.readlines()
                c = input('Введите id человека: ')
                if y1 == 'да' or y1 == 'Да':
                    Find2(a,c)
                elif y1 == 'нет' or y1 == 'Нет':
                    Find1(a, c)
                elif not z:
                    print('Пользователь с таким id не найден')
        elif y == '1':
            with open('Semi_7\spravochnick.txt', 'r') as file:
                a = file.readlines()
                c = input('Введите имя фамилию человека: ')
                for i in a:
                    last = i.split()
                    if last[1] + ' ' + last[2] == c:
                        print(i)
        else:
            print(
                'Человек с таким именем или фамилией не найден или вы ввели неверный критерий')


def SortingFile():
    with open('Semi_7\spravochnick.txt', 'r') as file:
        a = file.readlines()
        f = sorted(a)
        for i in f:
            print(i)


def Find1(list, c):
    global z
    global f
    ress = ''
    for i in list:
        for j in range(0, len(i)):
            if i[j].isdigit():
                ress = ress + i[j]
            elif ress == c:
                z = True
                print(i)
                break
            elif i[j] == ' ' or f:
                f = True
                ress = ''
                break
    return z

def Find2(list, c):
    global z
    z = False
    ress = ''
    for i in list:
        for j in range(0, len(i)):
                if i[j].isdigit():
                    ress = ress + i[j]
                    f = False
                elif ress == c:
                    z = True
                    count = 0
                    for c in i:
                        for j in range(0, len(c)):
                            if c[j].isdigit():
                                continue
                            else:
                                if count >= 3:
                                    break
                                print(c[j], end='')
                                if c[j] == ' ':
                                    count = count + 1
                elif i[j] == ' ' or f:
                    f = True
                    ress = ''
                    continue
    return z
