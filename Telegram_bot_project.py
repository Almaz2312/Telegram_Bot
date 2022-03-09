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
    btn_1 = types.InlineKeyboardButton(imghdr='data:image/png;base64,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' ,text='Смартфон', callback_data='смартфон')
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

<<<<<<< HEAD

@bot.message_handler(content_types=['text'])    # Все 3 функции вставил в одну.
def model(message):                             # Повторяющиеся функции вписал в одну и вызывал их внизу.
=======
        
@bot.message_handler(content_types=['text'])
def model(message):
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
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
<<<<<<< HEAD
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'LIFEBOOK U7311':
<<<<<<< HEAD
        text = f'Intel Core i5-1135G7, RAM: 16GB, 512GB SSD, The Intel Iris Xe Graphics G7 (80 EUs). Цена: 2100 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'Intel Core i5-1135G7, RAM: 16GB, 512GB SSD, The Intel Iris Xe Graphics G7 (80 EUs). Цена: 2100 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'LIFEBOOK U7411':
<<<<<<< HEAD
        text = f'Intel Core i5-1145G7, RAM: 16GB, 512GB SSD, The Intel Iris Xe Graphics G7. Цена: 2100 USD 1500 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'Intel Core i5-1145G7, RAM: 16GB, 512GB SSD, The Intel Iris Xe Graphics G7. Цена: 2100 USD 1500 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'ExpertBook':
<<<<<<< HEAD
        text = f'Intel i7-1165G7, RAM: 16GB, 1T SSD, Intel Iris. Цена: 2050 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'Intel i7-1165G7, RAM: 16GB, 1T SSD, Intel Iris. Цена: 2050 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'ASUSPRO':
<<<<<<< HEAD
        text = f'Pentium N6000, RAM: 4GB, 128GB SSD, Intel UHD Graphics. Цена: 400 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'Pentium N6000, RAM: 4GB, 128GB SSD, Intel UHD Graphics. Цена: 400 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'ZenBook':
<<<<<<< HEAD
        text = f'Intel i7-1165G7, RAM: 16GB, 1T SSD, Intel Iris XE Graphics. Цена: 1500 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'Intel i7-1165G7, RAM: 16GB, 1T SSD, Intel Iris XE Graphics. Цена: 1500 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Ideapad 3':
<<<<<<< HEAD
        text = f'Intel Core i7-1165G7, RAM: 20GB, 1T SSD, Intel NVIDIA MX450. Цена: 1000 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'Intel Core i7-1165G7, RAM: 20GB, 1T SSD, Intel NVIDIA MX450. Цена: 1000 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Thinkpad X1 Yoga Gen 5':
<<<<<<< HEAD
        text = f'Intel Core i5-10210U, RAM: 8GB, 256GB SSD, UHD Graphics 620. Цена: 1700 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'Intel Core i5-10210U, RAM: 8GB, 256GB SSD, UHD Graphics 620. Цена: 1700 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Ideapad Gaming 3':
<<<<<<< HEAD
        text = f'AMD Ryzen 5 4600H, RAM: 32GB DDR, 512B SSD, NVIDIA GeForce GTX1650. Цена: 1100 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'AMD Ryzen 5 4600H, RAM: 32GB DDR, 512B SSD, NVIDIA GeForce GTX1650. Цена: 1100 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Xiaomi Redmi 9A':
<<<<<<< HEAD
        text = f'RAM:4, 32GB, Sky Blue. Цена: 120 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'RAM:4, 32GB, Sky Blue. Цена: 120 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Xiaomi Redmi 10':
<<<<<<< HEAD
        text = f'RAM:4, 128GB, Sea Blue. Цена: 250 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'RAM:4, 128GB, Sea Blue. Цена: 250 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Xiaomi Redmi Note 9':
<<<<<<< HEAD
        text = f'RAM:4, 128GB, Polar White. Цена: 200 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'RAM:4, 128GB, Polar White. Цена: 200 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Iphone 13':
<<<<<<< HEAD
        text = f'128GB. Цена: 930 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'128GB. Цена: 930 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Iphone 12':
<<<<<<< HEAD
        text = f'128GB. Цена: 830 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'128GB. Цена: 830 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Iphone 11':
<<<<<<< HEAD
        text = f'128GB. Цена: 700 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'128GB. Цена: 700 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Samsung Galaxy A22':
<<<<<<< HEAD
        text = f'RAM:4, 64GB. Цена: 220 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'RAM:4, 64GB. Цена: 220 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Samsung Galaxy A12(A125)':
<<<<<<< HEAD
        text = f'RAM:4, 64GB. Цена: 170 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'RAM:4, 64GB. Цена: 170 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Samsung Galaxy Note 10':
<<<<<<< HEAD
        text = f'RAM:4, 64GB. Цена: 850 USD.' \
               f' Вы уверены что хотите купить этот - {message.text}?'
=======
        text = f'RAM:4, 64GB. Цена: 850 USD' \
               f'Вы уверены что хотите купить этот - {message.text}'
>>>>>>> 7b3862a0e86772984a5c513077f0cf6258b169d2
        bot.send_message(message.chat.id, text,
                         reply_markup=choice)

    if message.text == 'Да':
        bot.send_message(message.chat.id,
                         'Спасибо за покупку!!!'
                         ' Наш представитель свяжется с вами!!!')

    if message.text == 'Нет':
        bot.send_message(message.chat.id,
                         'Спасибо за ваше время!!!'
                         ' Будем рады видеть снова!!!')


bot.infinity_polling()