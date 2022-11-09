# Напишите программу, удаляющую из текста все слова, содержащие "абв".

import telebot

def deleting(text):
    while text.find('абв') != -1:
        text = text.replace('абв', '')
    return text

bot = telebot.TeleBot("5703355736:AAEEK1seScMfcqODF_p6W3D1iJepTvJdCYc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, deleting(message.text))

bot.infinity_polling()