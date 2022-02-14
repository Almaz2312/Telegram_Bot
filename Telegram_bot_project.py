# """
# Задание на написание бота
# """

import telebot
from decouple import config
from telebot import types


bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)


@bot.message_handler(commands=["start", 'hi'])
def answer_starts(message):
    text = f"Добро пажаловать в магазин электроники {message.from_user.first_name}"\
            f"{message.from_user.last_name}!!!"\
           f" Выберите категорию"
    keyword_in = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='Смартфон', callback_data='смартфон')
    btn_2 = types.InlineKeyboardButton(text='Ноутбук', callback_data='ноутбук')
    keyword_in.add(btn_1, btn_2)
    bot.send_message(message.chat.id, text, reply_markup=keyword_in)


@bot.callback_query_handler(func=lambda call: True)
def send_cource(call):
    if call.data == 'смартфон':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Redmi')
        btn_2 = types.KeyboardButton('Apple')
        btn_3 = types.KeyboardButton('Samsung')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали {call.data}! теперь необходимо выбрать модель!!!'
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )

    if call.data == 'ноутбук':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Fujitsu')
        btn_2 = types.KeyboardButton('Asus')
        btn_3 = types.KeyboardButton('lenovo')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали {call.data}! теперь необходимо выбрать модель!!!'
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )

