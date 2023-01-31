import telebot
from telebot import types
import random
import emoji 

bot = telebot.TeleBot('6064045768:AAGMIEr871yK_LIpoSKuM5EVYF2upeFMhS0')
candys = 221


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Напиши 'Погнали' и мы начнём!")


@bot.message_handler(content_types="text")
def lot(message):
    global candys
    a = ['Тебе',"Боту"]
    z = random.choice(a)
    if z == 'Тебе':
        bot.send_message(message.chat.id, f'Первый ход достаётся {z}, cколько конфет возьмёшь?')
        bot.register_next_step_handler(message, next_step)
    if z == 'Боту':
        bot.send_message(message.chat.id, f'Первый ход достаётся {z}, Бот берёт {candys%29} конфет. Сколько конфет возьмёшь ты?')
        candys -= candys%29
        bot.register_next_step_handler(message, step_two)
        
        



def next_step(message):
    global candys
    turn = int(message.text)
    if turn > 28 or turn < 1:
        candys = 221
        bot.send_message(message.chat.id, 'Ты взял слишком много или слишком мало, поэтому придётся начать заново. Напиши "Ещё раз" и мы начнём!')
        bot.register_next_step_handler(message,lot)
        return
    candys -= turn
    if turn == 18:
        bot_iq = random.randint(1,28)
    else:
        bot_iq = candys % 29
    candys -= bot_iq
    bot.send_message(
        message.chat.id, f'Твой оппонент взял {bot_iq} конфет, осталось {candys}')
    bot.send_message(message.chat.id, 'Сколько конфет возьмёшь?')
    bot.register_next_step_handler(message, step_two)


def step_two(message):
    global candys
    turn = int(message.text)
    if turn > 28 or turn < 1:
        candys = 221
        bot.send_message(message.chat.id, 'Ты взял слишком много или слишком мало, поэтому придётся начать заново. Напиши "Ещё раз" и мы начнём!')
        bot.register_next_step_handler(message,lot)
        return
    candys -= turn
    if candys <= 0:
        bot.send_message(
        message.chat.id, f'Поздравляю тебя с победой!')
        candys = 221
        return
    bot_iq = 29 - turn
    candys -= bot_iq
    if candys <= 0:
        bot.send_message(
        message.chat.id, emoji.emojize('Твой соперник забрал все конфеты :pensive:',language='alias')) #pip install emoji
        candys = 221
        return
    bot.send_message(
        message.chat.id, f'Твой оппонент взял {bot_iq} конфет, осталось {candys}')
    bot.send_message(message.chat.id, 'Сколько конфет возьмёшь?')
    bot.register_next_step_handler(message, step_three)


def step_three(message):
    global candys
    turn = int(message.text)
    if turn > 28 or turn < 1:
        candys = 221
        bot.send_message(message.chat.id, 'Ты взял слишком много или слишком мало, поэтому придётся начать заново. Напиши "Ещё раз" и мы начнём!')
        bot.register_next_step_handler(message,lot)
        return
    candys -= turn
    if candys <= 0:
        candys = 221
        bot.send_message(
        message.chat.id, emoji.emojize('Поздравляю тебя с победой!:tada:',language = 'alias'))
        return
    bot_iq = 29 - turn
    candys -= bot_iq
    if candys <= 0:
        candys = 221
        bot.send_message(
        message.chat.id, emoji.emojize('Твой соперник забрал все конфеты :pensive:'))
        return
    bot.send_message(
        message.chat.id, f'Твой оппонент взял {bot_iq} конфет, осталось {candys}')
    bot.send_message(message.chat.id, 'Сколько конфет возьмёшь?')
    bot.register_next_step_handler(message, step_two)


bot.infinity_polling()