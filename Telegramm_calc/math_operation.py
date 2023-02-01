from bot_main import *
import telebot




def SumNumFloat(message):
    global a 
    global b
    log(message) 
    text = message.text
    vssc = text.split()
    a = float(vssc[0])
    b = float(vssc[1])
    bot.send_message(message.chat.id,f"{a} + {b} = {a+b}")
    start(message)



def SubNumFloat(message):
    global a
    log(message) 
    text = message.text
    vssc = text.split()
    a = float(vssc[0])
    b = float(vssc[1])
    bot.send_message(message.chat.id,f"{a} - {b} = {a - b}")
    start(message)

def DivideFloat(message):
    global a 
    log(message) 
    text = message.text
    vvs = text.split()
    a = float(vvs[0])
    b = float(vvs[1])
    bot.send_message(message.chat.id,f'{a} : {b} = {a / b}')
    start(message)

 

def MultiFloat(message):
    log(message) 
    global a
    text = message.text
    values = text.split()
    a = float(values[0])
    b = float(values[1])
    bot.send_message(message.chat.id,f'{a} * {b} = {a * b}')
    start(message)