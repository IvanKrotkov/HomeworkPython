from math_operation import *
# from bot_main import *
import telebot
from telebot import types 



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