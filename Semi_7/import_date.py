import random
list = []

def Init():
    global list
    list.append(random.randint(1,100))
    list.append(input("Введите имя: "))
    list.append(input("Введите Фамилию: "))
    list.append(input("Введите номер телефона: "))
    list.append(input("Введите комментарий: "))
    return list


    

