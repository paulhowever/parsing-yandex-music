import telebot
from telebot import types
from main import *

TOKEN = '6024741884:AAH9YysvTriwABngxIxyPs7RL2BzAtXkv-o'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    want = types.KeyboardButton('Хочу!')
    markup.add(want)
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать Топ 100 чарта Yandex Music? Нажимай на Хочу!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Хочу!':
            deleteMarkup = telebot.types.ReplyKeyboardRemove()

            def getResult(message):
                global countTracks
                countTracks = message.text
                lstTracks = lst[0:int(countTracks)]
                topChart = '\n'.join(lstTracks)
                bot.send_message(chat_id=message.chat.id, text=topChart)

            msg = bot.send_message(message.chat.id, 'Напишите количество треков, которое хотите увидеть', reply_markup=deleteMarkup)
            bot.register_next_step_handler(msg, getResult)

    else: bot.send_message(message.chat.id, 'я вас не понял((')

bot.polling(none_stop=True)
