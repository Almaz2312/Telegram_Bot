"""
Задание на написание бота
"""

import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)

@bot.message_handler(commands=["start", 'HI'])
def answer_starts(message):
    text = f"Добро пажаловать в магазин электроники {message.from_user.first_name}"\
            f"{message.from_user.last_name}!!!"\
           f" Выберите категорию"
    keyword_in = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='Смартфон', callback_data='смартфон')
    btn_2 = types.InlineKeyboardButton(text='Ноутбук', callback_data='ноутбук')
    keyword_in.add(btn_1, btn_2)
    bot.send_message(message.chat.id, text, reply_markup=keyword_in)

@bot.callback_query_handler(func=lambda call:True)
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
        btn_1 = types.KeyboardButton('Fujtsu')
        btn_2 = types.KeyboardButton('Asus')
        btn_3 = types.KeyboardButton('lenovo')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали {call.data}! теперь необходимо выбрать модель!!!'
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )

        
@bot.message_handler(content_types=['text'])
def model(message):
    choice = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_yes = 'Да'
    btn_no = 'Нет'
    choice.add(btn_yes, btn_no)
    if message.text == 'Fujitsu':
        fujitsu_model = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('LIFEBOOK U9311')
        btn_2 = types.KeyboardButton('LIFEBOOK U7311')
        btn_3 = types.KeyboardButton('LIFEBOOK U7411')
        fujitsu_model.add(btn_1, btn_2, btn_3)
        text = f'Выберите модель {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=fujitsu_model
                         )

    if message.text == 'Asus':
        asus_model = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('ExpertBook')
        btn_2 = types.KeyboardButton('ASUSPRO')
        btn_3 = types.KeyboardButton('ZenBook')
        asus_model.add(btn_1, btn_2, btn_3)
        text = f'Выберите модель {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=asus_model
                         )

    if message.text == 'lenovo':
        lenovo_model = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Ideapad 3')
        btn_2 = types.KeyboardButton('Thinkpad X1 Yoga Gen 5')
        btn_3 = types.KeyboardButton('Ideapad Gaming 3')
        lenovo_model.add(btn_1, btn_2, btn_3)
        text = f'Выберите модель {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=lenovo_model
                         )

    if message.text == 'Redmi':
        redmi_model = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Xiaomi Redmi 9A')
        btn_2 = types.KeyboardButton('Xiaomi Redmi 10')
        btn_3 = types.KeyboardButton('Xiaomi Redmi Note 9')
        redmi_model.add(btn_1, btn_2, btn_3)
        text = f'Выберите модель {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=redmi_model
                         )

    if message.text == 'Apple':
        apple_model = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Iphone 13')
        btn_2 = types.KeyboardButton('Iphone 12')
        btn_3 = types.KeyboardButton('Iphone 11')
        apple_model.add(btn_1, btn_2, btn_3)
        text = f'Выберите модель {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=apple_model
                         )

    if message.text == 'Samsung':
        samsung_model = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Samsung Galaxy A22')
        btn_2 = types.KeyboardButton('Samsung Galaxy A12(A125)')
        btn_3 = types.KeyboardButton('Samsung Galaxy Note 10')
        samsung_model.add(btn_1, btn_2, btn_3)
        text = f'Выберите модель {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=samsung_model
                         )


    if message.text == 'LIFEBOOK U9311':
        text = f'Intel  Core i7-1185G7, RAM: 32GB, 1TB SSD, The Intel Iris Xe Graphics. Цена: 2500 USD.' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'LIFEBOOK U7311':
        text = f'Intel Core i5-1135G7, RAM: 16GB, 512GB SSD, The Intel Iris Xe Graphics G7 (80 EUs). Цена: 2100 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'LIFEBOOK U7411':
        text = f'Intel Core i5-1145G7, RAM: 16GB, 512GB SSD, The Intel Iris Xe Graphics G7. Цена: 2100 USD 1500 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'ExpertBook':
        text = f'Intel i7-1165G7, RAM: 16GB, 1T SSD, Intel Iris. Цена: 2050 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'ASUSPRO':
        text = f'Pentium N6000, RAM: 4GB, 128GB SSD, Intel UHD Graphics. Цена: 400 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'ZenBook':
        text = f'Intel i7-1165G7, RAM: 16GB, 1T SSD, Intel Iris XE Graphics. Цена: 1500 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Ideapad 3':
        text = f'Intel Core i7-1165G7, RAM: 20GB, 1T SSD, Intel NVIDIA MX450. Цена: 1000 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Thinkpad X1 Yoga Gen 5':
        text = f'Intel Core i5-10210U, RAM: 8GB, 256GB SSD, UHD Graphics 620. Цена: 1700 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Ideapad Gaming 3':
        text = f'AMD Ryzen 5 4600H, RAM: 32GB DDR, 512B SSD, NVIDIA GeForce GTX1650. Цена: 1100 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Xiaomi Redmi 9A':
        text = f'RAM:4, 32GB, Sky Blue. Цена: 120 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Xiaomi Redmi 10':
        text = f'RAM:4, 128GB, Sea Blue. Цена: 250 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Xiaomi Redmi Note 9':
        text = f'RAM:4, 128GB, Polar White. Цена: 200 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Iphone 13':
        text = f'128GB. Цена: 930 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Iphone 12':
        text = f'128GB. Цена: 830 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Iphone 11':
        text = f'128GB. Цена: 700 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Samsung Galaxy A22':
        text = f'RAM:4, 64GB. Цена: 220 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Samsung Galaxy A12(A125)':
        text = f'RAM:4, 64GB. Цена: 170 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Samsung Galaxy Note 10':
        text = f'RAM:4, 64GB. Цена: 850 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)


    if message.text == 'Да':
        bot.send_message(message.chat.id,
                         'Спасибо за покупку!!!'
                         'Наш представитель свяжется с вами!!!')
    if message.text == 'Нет':
        bot.send_message(message.chat.id,
                         'Спасибо за ваше время!!!'
                         'Будем рады видеть снова!!!')


bot.infinity_polling()
