import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)


@bot.message_handler(commands=["start", "Hi", "hi"])    # Выбираем на что будет отвечать бот
def answer_start(message):
    print(message.from_user.id)
    text = f'Добро пожаловать {message.from_user.first_name}"' \
           f'{message.from_user.last_name}!!! ' \
           f'Выберите тот курс на который хотите пойти'
    keyboard_in = types.InlineKeyboardMarkup()          # Создаёт образ кнопки
    btn_1 = types.InlineKeyboardButton(text='Python', callback_data='python')
    btn_2 = types.InlineKeyboardButton(text='Java', callback_data='java')
    btn_3 = types.InlineKeyboardButton(text='C#', callback_data='C#')
    keyboard_in.add(btn_1, btn_2, btn_3)
    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)


@bot.callback_query_handler(func=lambda call:True)
def send_course(call):
    if call.data:
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton(f'{call.data} morning')
        btn_2 = types.KeyboardButton(f'{call.data} evening')
        btn_3 = types.KeyboardButton(f'{call.data} bootcamp')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали {call.data}!, теперь необходимо выбрать группу'
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )

@bot.message_handler(content_types=['text'])
def send_good_message(message):
    if message.text:
        bot.send_message(message.chat.id,
                         f'Вас записали на курс {message.text}!'
                         'Менеджер с вами свяжется!')


bot.polling()


# Задача сделать с Java тоже самое что и с питоном


