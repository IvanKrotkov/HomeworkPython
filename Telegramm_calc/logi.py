import telebot
from telebot import types
import datetime

def log(message):
    file = open('Telegramm_calc\logCalc.csv','a')
    file.write(f'id: {message.from_user.id} Name: {message.from_user.first_name} text: {message.text} date: {datetime.datetime.now()} \n')
    file.close()

