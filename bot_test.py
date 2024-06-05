
import telebot
import json
from datetime import datetime

# Инициализируем бота
bot = telebot.TeleBot("6915777848:AAEirlOMfM1Ea7xmCe2otx8GGJ0jbb_iGkg")

# Загружаем списки тегов и ФИО из файлов
with open('C:/Users/Home/Desktop/Бот выпускной/tags.txt', 'r', encoding="UTF-8") as file:
    username_list = file.read()

with open("C:/Users/Home/Desktop/Бот выпускной/ФИО 4 курс.txt", 'r', encoding="UTF-8") as file:
    names_list = file.read()


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Введи свои ФИО. Если отчества нет - введите прочерк("-")')

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def check_info(message):
    # Получаем id и username пользователя
    user_id = message.from_user.id
    username = message.from_user.username

    # Разделяем сообщение на ФИО
    data = message.text.split()
    if len(data) != 3:
        bot.reply_to(message, 'Неверный формат ввода. Пожалуйста, введи ФИО через пробел (Фамилия Имя Отчество). Если отчества нет - введи прочерк("-")')
        return

    full_name = " ".join(data)

       # Проверяем наличие ФИО в списке
    if full_name in names_list:
        # Проверяем наличие username в списке
        if username in username_list:
            # Составляем словарь для записи в JSON файл
            info = {
                f'@{username}': [data[0], data[1], data[2], "-", "-", "-", datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            }

            # Записываем данные в JSON файл
            with open("C:/Users/Home/Desktop/Бот выпускной/data.json", 'w') as file:
                json.dump(info, file, ensure_ascii=False, indent=4)

            bot.reply_to(message, 'Данные успешно записаны в файл data.json.')
        else:
            bot.reply_to(message, 'Извини, твоего username нет в списке. Обратись в личные сообщения.')
    else:
        bot.reply_to(message, 'Извини, твоих данных нет в списке четверокурсников. Обратись в личные сообщения.')

# Запускаем бота
bot.polling(none_stop=True)
