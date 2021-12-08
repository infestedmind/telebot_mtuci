import telebot

from config import TOKEN
from commands.timetable import timetable

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["р"])
def start(message):
    rasp = timetable(message=message.text)
    bot.send_message(message.chat.id, rasp)

bot.infinity_polling()