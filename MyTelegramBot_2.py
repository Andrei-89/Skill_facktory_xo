import telebot

TOKEN = "6001384846:AAFalCEEuvCw13PDd3eIKHmXlKdXWD8as4Y"
bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True)


@bot.message_handler(content_types=['text'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}!")
