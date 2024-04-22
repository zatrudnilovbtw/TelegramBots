import telebot
from telebot import types
from datetime import datetime, timedelta

API_TOKEN = 'ur token'
bot = telebot.TeleBot(API_TOKEN)

# Словарь для хранения количества кликов пользователей за определенные периоды
clicks = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('клик')
    itembtn2 = types.KeyboardButton('Количество')
    itembtn3 = types.KeyboardButton('Сбросить счетчик')  # Добавляем новую кнопку
    markup.add(itembtn1, itembtn2, itembtn3)  # Добавляем новую кнопку в клавиатуру
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.from_user.id
    if message.text == 'клик':
        # Увеличиваем счетчик кликов для пользователя
        if user_id not in clicks:
            clicks[user_id] = {'hour': 0, 'day': 0, 'month': 0}
        clicks[user_id]['hour'] += 1
        clicks[user_id]['day'] += 1
        clicks[user_id]['month'] += 1
        bot.reply_to(message, "+1")
    elif message.text == 'Количество':
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(types.InlineKeyboardButton("За час", callback_data='hour'),
                   types.InlineKeyboardButton("За день", callback_data='day'),
                   types.InlineKeyboardButton("За месяц", callback_data='month'))
        bot.send_message(message.chat.id, "Выберите период:", reply_markup=markup)
    elif message.text == 'Сбросить счетчик':  # Обработка нажатия на кнопку "Сбросить счетчик"
        if user_id in clicks:
            clicks[user_id] = {'hour': 0, 'day': 0, 'month': 0}
        bot.reply_to(message, "Счетчик сброшен.")

# Обработчик нажатия на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id
    if user_id not in clicks:
        clicks[user_id] = {'hour': 0, 'day': 0, 'month': 0}
    if call.data in clicks[user_id]:
        bot.answer_callback_query(call.id, f"Вы кликнули{clicks[user_id][call.data]} раз(а) за {call.data}")

# Запуск бота
bot.polling()