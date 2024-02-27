import telebot
from telebot import types




TOKEN = '6805462847:AAH3ePWEDuTCFYKJ-pSVjNyKTi9hHMFpVvY'
bot = telebot.TeleBot(TOKEN)

phones = {
        'Realme XT': {'ОС': 'Android', 'ОЗУ': '4 ГБ / 6 ГБ / 8 ГБ', 'Память': '64 ГБ / 128 ГБ', 'Дисплей': '6,4 дюйма, Super AMOLED', 'Камера': 'Четыре основные камеры: 64 МП + 8 МП + 2 МП + 2 МП, фронтальная камера: 16 МП', 'Батарея': '4000 мАч', 'Тип дисплея': 'Super AMOLED', 'Процессор': 'Qualcomm Snapdragon 712', 'Размер экрана': '6,4 дюйма' ,  'Фото': 'https://goo.su/QHnfZIt'},
        'Honor 10 lite': {'ОС': 'Android', 'ОЗУ': '4 ГБ', 'Память': '64 ГБ', 'Дисплей': '6,21 дюйма, IPS LCD', 'Камера': 'Двойная 13 МП + 2 МП', 'Батарея': '3400 мАч', 'Тип дисплея': 'IPS LCD', 'Процессор': 'HiSilicon Kirin 710', 'Размер экрана': '6,21 дюйма', 'Фото': 'https://goo.su/h5mDz'  },
        'Google Pixel 6 Pro': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '128 ГБ', 'Дисплей': '6,7 дюйма, LTPO OLED', 'Камера': '50 МП двойная камера', 'Батарея': '5003 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Tensor SoC', 'Размер экрана': '6,7 дюйма', 'Фото': 'https://goo.su/ebJiVYe'},
        'Xiaomi Mi 11 Ultra': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '256 ГБ', 'Дисплей': '6,81 дюйма, AMOLED', 'Камера': '50 МП Тройная камера', 'Батарея': '5000 мАч', 'Тип дисплея': 'AMOLED', 'Процессор': 'Snapdragon 888', 'Размер экрана': '6,81 дюйма','Фото': 'https://goo.su/c2EJW0U'},
        'iPhone 13 mini': {'ОС': 'iOS', 'ОЗУ': '4 ГБ', 'Память': '64 ГБ', 'Дисплей': '5,4 дюйма, Super Retina XDR', 'Камера': 'Двойная 12 МП система', 'Батарея': '2438 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'A15 Bionic', 'Размер экрана': '5,4 дюйма','Фото': 'https://goo.su/tke8Hh',},
        'Samsung Galaxy Z Fold 3': {'ОС': 'Android', 'ОЗУ': '12 ГБ', 'Память': '256 ГБ', 'Дисплей': '7,6 дюйма (раскрытый), AMOLED', 'Камера': 'Тройная 12 МП система', 'Батарея': '4400 мАч', 'Тип дисплея': 'AMOLED', 'Процессор': 'Snapdragon 888', 'Размер экрана': '7,6 дюйма (раскрытый)','Фото': 'https://goo.su/sIL8vws'},
        'Sony Xperia 1' : {'ОС': 'Android', 'ОЗУ': '12 ГБ', 'Память': '256 ГБ', 'Дисплей': '6,5 дюйма, 4K HDR OLED', 'Камера': 'Тройная 12 МП система', 'Батарея': '4500 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Snapdragon 888', 'Размер экрана': '6,5 дюйма','Фото': 'https://goo.su/stoYAKT'},
        'Huawei P50 Pro': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '256 ГБ', 'Дисплей': '6,6 дюйма, OLED', 'Камера': 'Квадрокамера 50 МП', 'Батарея': '4360 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Kirin 9000', 'Размер экрана': '6,6 дюйма', 'Фото': 'https://goo.su/fODXJ'},
        'Samsung Galaxy S21 Ultra': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '128 ГБ', 'Дисплей': '6,7 дюйма, LTPO OLED', 'Камера': '50 МП двойная камера', 'Батарея': '4900 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Tensor SoC', 'Размер экрана': '6,7 дюйма','Фото': 'https://goo.su/bJVkZX'},
        'OnePlus 9': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '128 ГБ', 'Дисплей': '6,7 дюйма, LTPO OLED', 'Камера': '50 МП двойная камера', 'Батарея': '4700 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Tensor SoC', 'Размер экрана': '6,7 дюйма','Фото': 'https://goo.su/eojR'},
        'Xiaomi Redmi Note 10': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '128 ГБ', 'Дисплей': '6,7 дюйма, LTPO OLED', 'Камера': '50 МП двойная камера', 'Батарея': ' 5000 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Tensor SoC', 'Размер экрана': '6,7 дюйма','Фото': 'https://goo.su/TWDLUjS'},
        'Google Pixel 5': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '128 ГБ', 'Дисплей': '5,7 дюйма, LTPO OLED', 'Камера': '50 МП двойная камера', 'Батарея': '5003 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Tensor SoC', 'Размер экрана': '6,7 дюйма','Фото': 'https://goo.su/ebJiVYe'},
        'Sony Xperia 5': {'ОС': 'Android', 'ОЗУ': '8 ГБ', 'Память': '128 ГБ', 'Дисплей': '6,5 дюйма, LTPO OLED', 'Камера': '30 МП двойная камера', 'Батарея': ' 5000 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'Tensor SoC', 'Размер экрана': '6,7 дюйма','Фото': 'https://goo.su/v9BlbzE'},
        'Iphone 13 Pro Max': {'ОС': 'iOS', 'ОЗУ': '6 ГБ', 'Память': '128 ГБ', 'Дисплей': '6,7 дюйма, Super Retina XDR', 'Камера': 'Тройная 12 МП система', 'Батарея': '4352 мАч', 'Тип дисплея': 'OLED', 'Процессор': 'A15 Bionic', 'Размер экрана': '6,7 дюйма','Фото': 'https://goo.su/6u9gOx1'},
         }






@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = [types.KeyboardButton(name) for name in phones.keys()]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Привет! Выберите телефон:', reply_markup=keyboard)



@bot.message_handler(func=lambda message: True)
def handle_text(message):
    phone_name = message.text.strip()

    if phone_name in phones:
        characteristics = phones[phone_name]
        response = f" {phone_name}:\n"
        for key, value in characteristics.items():
            response += f"{key}: {value}\n"

    else:
        response = f"Телефон '{phone_name}' не найден в базе данных, проверь правильность написания модели."

    bot.send_message(message.chat.id, response)

if __name__ == '__main__':
    bot.polling(none_stop=True)


















































