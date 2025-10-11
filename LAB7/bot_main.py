import telebot
import os
from dotenv import load_dotenv
load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(func=lambda a: True) #func=labda завжди повертає True(пропускає всі смс)
def echo(a):
    bot.reply_to(a, a.text) #a(обєкт там де id,час), a.text(сам текст)
print('launch')
bot.infinity_polling() #безкінечно перевіряє, чи прийшло нове повідомлення
