import telebot
from telebot import types
from logi import * 





bot = telebot.TeleBot('6017054568:AAEwGY4VTOE6uGmronasRWIP-hJlPlgKy-A')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'C какими числами вы работаете? \n/rational - рациональные\n/int - натуральные\n/complex - комплексные')
    log(message) 

@bot.message_handler(commands=['rational'])
def nextstep(message):
    log(message) 
    buttonFloat(message)
@bot.message_handler(commands=['complex'])
def nextstep(message):
    log(message) 
    buttonComplex(message)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Список команд \n/start\n/rational\n/int\n/complex')
    log(message) 

@bot.message_handler(commands = ['int'])
def button(message):
    bot.send_message(message.chat.id,'Выберите операцию: \n 1 - cложение \n 2 - вычитание \n 3 - деление без остатка(только для целых чисел) \n 4 - остаток от деления(только для целых чисел)  \n 5 - деление \n 6 - умножение')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("1")
    but2 = types.KeyboardButton("2")
    but3 = types.KeyboardButton("3")
    but4 = types.KeyboardButton("4")
    but5 = types.KeyboardButton("5")
    but6 = types.KeyboardButton("6")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)
    markup.add(but6)
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)
    

@bot.message_handler(content_types = "text")
def controller(message):
    log(message) 
    if message.text == "1":
        bot.send_message(message.chat.id,"Введите два числа через пробел")
        bot.register_next_step_handler(message,SumNum)
    elif message.text == "2":
        bot.send_message(message.chat.id,"Введите два числа через пробел")
        bot.register_next_step_handler(message,SubNum)
    elif message.text == '3':
        bot.send_message(message.chat.id,'Введите два числа через пробел')
        bot.register_next_step_handler(message,DivideWithoutRemind)
    elif message.text == '4':
        bot.send_message(message.chat.id,'Введите два числа через пробел')
        bot.register_next_step_handler(message,Remind)
    elif message.text == '5':
        bot.send_message(message.chat.id,'Введите два числа через пробел')
        bot.register_next_step_handler(message,Divide)
    elif message.text == '6':
        bot.send_message(message.chat.id,'Введите два числа через пробел')
        bot.register_next_step_handler(message,Multi)    


def SumNum(message):
    global a 
    global b
    log(message) 
    text = message.text
    vssc = text.split()
    a = int(vssc[0])
    b = int(vssc[1])
    bot.send_message(message.chat.id,f"{a} + {b} = {a+b}")
    start(message)



def SubNum(message):
    global a
    log(message) 
    text = message.text
    vssc = text.split()
    a = int(vssc[0])
    b = int(vssc[1])
    bot.send_message(message.chat.id,f"{a} - {b} = {a - b}")
    start(message)

def Divide(message):
    global a 
    log(message) 
    text = message.text
    vvs = text.split()
    a = int(vvs[0])
    b = int(vvs[1])
    bot.send_message(message.chat.id,f'{a} : {b} = {a / b}')
    start(message)

 

def DivideWithoutRemind(message):
    log(message) 
    text = message.text
    values = text.split()
    a = int(values[0])
    b = int(values[1])
    bot.send_message(message.chat.id,f'{a} // {b} = {a // b}')
    start(message) 


def Remind(message):
    log(message) 
    text = message.text
    values = text.split()
    a = int(values[0])
    b = int(values[1])
    bot.send_message(message.chat.id,f'Остаток от деления {a} на {b} = {a % b}') 
    start(message)


def Multi(message,type = int):
    log(message) 
    global a
    text = message.text
    values = text.split()
    a = type(values[0])
    b = type(values[1])
    bot.send_message(message.chat.id,f'{a} * {b} = {a * b}')
    start(message)
    

def buttonFloat(message):
    bot.send_message(message.chat.id,'Выберите операцию: \n1 - cложение\n2 - вычитание\n3 - деление \n4 - умножение')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("1")
    but2 = types.KeyboardButton("2")
    but5 = types.KeyboardButton("3")
    but6 = types.KeyboardButton("4")
    markup.add(but1)
    markup.add(but2)
    markup.add(but5)
    markup.add(but6)
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)
    bot.register_next_step_handler(message, controllerFloat)

def buttonComplex(message):
    bot.send_message(message.chat.id,'Выберите операцию: \n1 - cложение\n2 - вычитание\n3 - деление \n4 - умножение')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("1")
    but2 = types.KeyboardButton("2")
    but5 = types.KeyboardButton("3")
    but6 = types.KeyboardButton("4")
    markup.add(but1)
    markup.add(but2)
    markup.add(but5)
    markup.add(but6)
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)
    bot.register_next_step_handler(message, controllerComplex)


def controllerComplex(message):
    log(message) 
    if message.text == "1":
        bot.send_message(message.chat.id,"Введите два числа через пробел\nНапример:\n27+2j 22+4j")
        bot.register_next_step_handler(message,SumNumComplex)
    elif message.text == "2":
        bot.send_message(message.chat.id,"Введите два числа через пробел\nНапример:\n27+2j 22+4j")
        bot.register_next_step_handler(message,SubNumComplex)
    elif message.text == '3':
        bot.send_message(message.chat.id,'Введите два числа через пробел\nНапример:\n27+2j 22+4j')
        bot.register_next_step_handler(message,DivideComplex)
    elif message.text == '4':
        bot.send_message(message.chat.id,'Введите два числа через пробел\nНапример:\n27+2j 22+4j')
        bot.register_next_step_handler(message,MultiComplex)


def controllerFloat(message):
    log(message) 
    if message.text == "1":
        bot.send_message(message.chat.id,"Введите два числа через пробел")
        bot.register_next_step_handler(message,SumNumFloat)
    elif message.text == "2":
        bot.send_message(message.chat.id,"Введите два числа через пробел")
        bot.register_next_step_handler(message,SubNumFloat)
    elif message.text == '3':
        bot.send_message(message.chat.id,'Введите два числа через пробел')
        bot.register_next_step_handler(message,DivideFloat)
    elif message.text == '4':
        bot.send_message(message.chat.id,'Введите два числа через пробел')
        bot.register_next_step_handler(message,MultiFloat)    
# Float
def SumNumFloat(message):
    global a 
    global b
    log(message) 
    text = message.text
    vssc = text.split()
    a = float(vssc[0])
    b = float(vssc[1])
    bot.send_message(message.chat.id,f"{a} + {b} = {round(a+b,3)}")
    start(message)



def SubNumFloat(message):
    global a
    log(message) 
    text = message.text
    vssc = text.split()
    a = float(vssc[0])
    b = float(vssc[1])
    bot.send_message(message.chat.id,f"{a} - {b} = {round(a - b,3)}")
    start(message)

def DivideFloat(message):
    global a 
    log(message) 
    text = message.text
    vvs = text.split()
    a = float(vvs[0])
    b = float(vvs[1])
    bot.send_message(message.chat.id,f'{a} : {b} = {round(a / b,3)}')
    start(message)

 

def MultiFloat(message):
    log(message) 
    global a
    text = message.text
    values = text.split()
    a = float(values[0])
    b = float(values[1])
    bot.send_message(message.chat.id,f'{a} * {b} = {round(a * b,3)}')
    start(message)


# complex


def SumNumComplex(message):
    global a 
    global b
    log(message) 
    text = message.text
    vssc = text.split()
    a = complex(vssc[0])
    b = complex(vssc[1])
    bot.send_message(message.chat.id,f"{a} + {b} = {a+b}")
    start(message)



def SubNumComplex(message):
    global a
    log(message) 
    text = message.text
    vssc = text.split()
    a = complex(vssc[0])
    b = complex(vssc[1])
    bot.send_message(message.chat.id,f"{a} - {b} = {a - b}")
    start(message)

def DivideComplex(message):
    global a 
    log(message) 
    text = message.text
    vvs = text.split()
    a = complex(vvs[0])
    b = complex(vvs[1])
    bot.send_message(message.chat.id,f'{a} : {b} = {a / b}')
    start(message)

 

def MultiComplex(message):
    log(message) 
    global a
    text = message.text
    values = text.split()
    a = complex(values[0])
    b = complex(values[1])
    bot.send_message(message.chat.id,f'{a} * {b} = {a * b}')
    start(message)

bot.infinity_polling()