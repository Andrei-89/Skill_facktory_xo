import telebot # общаемся с телеграммом через бота через api
from telebot import types
# import requests # для отправки http запросов на сервер
# import json # чтобы разбирать запросы, потому что ответ нам придет в формате json

TOKEN = "6211805317:AAGgz7jPMeFylK2AgHz_Ufstsxj_mKqpi_c"
bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=['text'])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}!")

@bot.message_handler(commands=['help'])
def send_welcome(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}")

@bot.message_handler(commands=['start'])
def button_message(message):
    send_welcome(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка 1")
    item2 = types.KeyboardButton("Кнопка 2")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите что вы хотите', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Кнопка 2":
        bot.send_message(message.chat.id, 'Спасибо за прочтение статьи!')

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)

