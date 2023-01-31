import telebot
from telebot import types
from logi import * 

typee = int

bot = telebot.TeleBot('6017054568:AAEwGY4VTOE6uGmronasRWIP-hJlPlgKy-A')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Список команд \n/start\n/button')
    log(message) 


@bot.message_handler(commands = ['button'])
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
    button(message)



def SubNum(message):
    global a
    log(message) 
    text = message.text
    vssc = text.split()
    a = int(vssc[0])
    b = int(vssc[1])
    bot.send_message(message.chat.id,f"{a} - {b} = {a - b}")
    button(message)

def Divide(message):
    global a 
    log(message) 
    text = message.text
    vvs = text.split()
    a = int(vvs[0])
    b = int(vvs[1])
    bot.send_message(message.chat.id,f'{a} : {b} = {a / b}')
    button(message)

 

def DivideWithoutRemind(message):
    log(message) 
    text = message.text
    values = text.split()
    a = int(values[0])
    b = int(values[1])
    bot.send_message(message.chat.id,f'{a} // {b} = {a // b}')
    button(message) 


def Remind(message):
    log(message) 
    text = message.text
    values = text.split()
    a = int(values[0])
    b = int(values[1])
    bot.send_message(message.chat.id,f'Остаток от деления {a} на {b} = {a % b}') 
    button(message)


def Multi(message):
    log(message) 
    global a
    text = message.text
    values = text.split()
    a = int(values[0])
    b = int(values[1])
    bot.send_message(message.chat.id,f'{a} * {b} = {a * b}')
    button(message)
    


bot.infinity_polling()