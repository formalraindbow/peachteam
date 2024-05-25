import telebot
from telebot import types
import json
from datetime import datetime
import pytz
API_TOKEN = '6581825456:AAHyqtmbJ94Scr-nui_oIUHuGYCkXUO2y3M'
bot = telebot.TeleBot(API_TOKEN)

data={}
university={}
vip_client=False
for_who = ""
for_where = ""

text_oplata = "Ты можешь приобрести билет на Ночь Социолога по одному из двух тарифов:\n\n_Junior_: проход на мероприятие и напиток при соблюдении дресс-кода! Стоимость: *1100*₽\n\n_Senior_: проход на мероприятие, напиток при соблюдении дресс-кода и три коктейля на твой выбор! Стоимость: *1700*₽\n\n*Повышение цен уже произошло!*\n\nВАЖНО: При покупке билета обязательно укажи *ФИО* и *свой ВУЗ* в сообщении к переводу.\n\nТИНЬКОФФ:\n'''5536 9141 2735 8780'''\n\nСБЕР:\n'''4276 3801 8332 1996'''\n\nПо номеру телефона:\n'''+7 (916) 342-73-92'''\nИлья Дмитриевич Ш.\n\n*ПОСЛЕ СОВЕРШЕНИЯ ОПЛАТЫ*\n\nПожалуйста, напиши свое *ФИО*\n\n_Пример: Иванов Иван Иваныч_\n\n_Если ты начал/а процесс регистрации, пожалуйста, пройди его до конца. Если после введения ФИО бот не дает  ответа - нажми заново /start_"
rules_dict = ['/home/romanloqi/code/правила_1 (1).png', '/home/romanloqi/code/правила_2 (1).png']
bar_dict= ['/home/romanloqi/code/photo_1.jpeg', '/home/romanloqi/code/photo_2.jpeg',
            '/home/romanloqi/code/photo_3.jpeg','/home/romanloqi/code/photo_4.jpeg',
            '/home/romanloqi/code/photo_5.jpeg', '/home/romanloqi/code/photo_6.jpeg',
            '/home/romanloqi/code/photo_7.jpeg', '/home/romanloqi/code/photo_8.jpeg']

loft = '/home/romanloqi/code/photo_loft.jpeg'
# меню для нс

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    global for_who, for_where
    if call.data == 'menu_da':
        start(call)
    elif call.data == 'da':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Проверка пройдена_", parse_mode="Markdown")
        priem_data(call)
    elif call.data == 'net':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Изменяем данные..._", parse_mode="Markdown")
        vozvrat(call)
    elif call.data == 'friends':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты узнал/ла о Ночи Социолога от друзей принята!_", parse_mode="Markdown")
        for_who = call.data
        razvodka_change_from_who(call)
    elif call.data == 'odnogroup':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты узнал/ла о Ночи Социолога от одногруппников/однокурсников принята!_", parse_mode="Markdown")
        for_who = call.data
        razvodka_change_from_who(call)
    elif call.data == 'social':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты узнал/ла о Ночи Социолога из соцсетей принята!_", parse_mode="Markdown")
        for_who = call.data
        razvodka_change_from_who(call)
    elif call.data == 'posvat':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты пришел/ла на Ночь Социолога побывав на посвяте принята!_", parse_mode="Markdown")
        for_who = call.data
        razvodka_change_from_who(call)
    elif call.data == 'another':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты узнал/ла о Ночи Социолога из другого источника принята!_", parse_mode="Markdown")
        for_who = call.data
        razvodka_change_from_who(call)
    elif call.data == 'social_studies':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты с факультета социальных наук принята!_", parse_mode="Markdown")
        for_where = call.data
        razvodka_change_facultet(call)
    elif call.data == 'computer_studies':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты с факультета компьютерных наук принята!_", parse_mode="Markdown")
        for_where = call.data
        razvodka_change_facultet(call)
    elif call.data == 'human_studies':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты с факультета гуманитарных наук принята!_", parse_mode="Markdown")
        for_where = call.data
        razvodka_change_facultet(call)
    elif call.data == 'natural_studies':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты с факультета естественных наук принята!_", parse_mode="Markdown")
        for_where = call.data
        razvodka_change_facultet(call)
    elif call.data == 'physical_studies':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты с факультета физических наук принята!_", parse_mode="Markdown")
        for_where = call.data
        razvodka_change_facultet(call)
    elif call.data == 'another_studies':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Информация о том, что ты с другого факультета или не учишься вузе принята!_", parse_mode="Markdown")
        for_where = call.data
        razvodka_change_facultet(call)
    elif call.data == 'menu_oplata':
        start(call)
    elif call.data == 'menu_info':
        start(call)
    elif call.data == 'bilet':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="Ты сможешь вернуться в главное меню после окончания регистрации!")
        buy_bilet(call)
    elif call.data == 'oplata':
        check_oplata(call)
    elif call.data =='info':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="Ты сможешь вернуться в главное меню после прочтения!")
        get_info(call)
    elif call.data =='change_data':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="Ты сможешь вернуться в главное меню после окончания изменений!")
        change_data(call)
    elif call.data =='change_fio':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Производятся изменения..._", parse_mode="Markdown")
        change_fio_kostyl(call)
    elif call.data =='change_university':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Производятся изменения..._", parse_mode="Markdown")
        change_university_kostyl(call)
    elif call.data =='change_facultet':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Производятся изменения..._", parse_mode="Markdown")
        change_facultet_kostyl(call)
    elif call.data =='change_from_who':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Производятся изменения..._", parse_mode="Markdown")
        change_from_who_kostyl(call)
    elif call.data =='change_another':
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="_Производятся изменения..._", parse_mode="Markdown")
        change_another_kostyl(call)
    elif call.data == 'menu_osninfo':
        menu_osninfo(call)
    elif call.data == 'menu_pravila':
        with open('/home/romanloqi/code/guest_page.json', 'r') as f:
            user_stat = json.load(f)
        chat_id_2 = call.message.chat.id
        if str(chat_id_2) not in user_stat:
            user_stat[str(chat_id_2)] = {"page_bar": 1, "page_rules": 1}
            with open('/home/romanloqi/code/guest_page.json', 'w') as f:
                json.dump(user_stat, f)
        menu_pravila(chat_id_2, user_stat)
    elif call.data == 'menu_bar':
        with open('/home/romanloqi/code/guest_page.json', 'r') as f:
            user_stat = json.load(f)
        chat_id_2 = call.message.chat.id
        if str(chat_id_2) not in user_stat:
            user_stat[str(chat_id_2)] = {"page_bar": 1, "page_rules": 1}
            with open('/home/romanloqi/code/guest_page.json', 'w') as f:
                json.dump(user_stat, f)
        menu_bar(chat_id_2, user_stat)
    elif call.data == 'menu_loft':
        menu_loft(call)
    elif call.data in ['prev_page_pr','next_page_pr']:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        count = len(rules_dict)
        with open('/home/romanloqi/code/guest_page.json', 'r') as f:
            user_stat = json.load(f)
        chat_id_2 = call.message.chat.id
        page = user_stat[str(chat_id_2)]["page_rules"]
        if call.data == 'prev_page_pr':
            page = page - 1 if page > 1 else count
        elif call.data == 'next_page_pr':
            page = page + 1 if page < count else 1
        user_stat[str(chat_id_2)]["page_rules"] = page
        with open('/home/romanloqi/code/guest_page.json', 'w') as of:
            json.dump(user_stat, of)
        menu_pravila(chat_id_2, user_stat)
    elif call.data in ['prev_page_bar','next_page_bar']:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        count = len(bar_dict)
        with open('/home/romanloqi/code/guest_page.json', 'r') as f:
            user_stat = json.load(f)
        chat_id_2 = call.message.chat.id
        page = user_stat[str(chat_id_2)]["page_bar"]
        if call.data == 'prev_page_bar':
            page = page - 1 if page > 1 else count
        elif call.data == 'next_page_bar':
            page = page + 1 if page < count else 1
        user_stat[str(chat_id_2)]["page_bar"] = page
        with open('/home/romanloqi/code/guest_page.json', 'w') as of:
            json.dump(user_stat, of)
        menu_bar(chat_id_2, user_stat)




def menu_loft(message):
    pagination = types.InlineKeyboardMarkup()
    # добавляю кнопочки
    btn_menu_bar = types.InlineKeyboardButton('Барная карта', callback_data='menu_bar')
    btn_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='menu_info')
    btn_menu_osninfo = types.InlineKeyboardButton(text='Основная инфа', callback_data='menu_osninfo')
    btn_menu_pravila = types.InlineKeyboardButton(text='Правила', callback_data='menu_pravila')
    pagination.add(btn_menu_bar, btn_menu_osninfo,  btn_menu, btn_menu_pravila)
    bot.send_photo(message.from_user.id, photo=open(loft, 'rb'), caption="План лофта",
                   reply_markup=pagination)


def menu_bar(chat_id_2, user_stat):
    pagination = types.InlineKeyboardMarkup()
    page = user_stat[str(chat_id_2)]["page_bar"]
    count = len(bar_dict)
    previous_button = types.InlineKeyboardButton('Назад', callback_data='prev_page_bar')
    next_button = types.InlineKeyboardButton('Вперед', callback_data='next_page_bar')
    btn_menu_osninfo = types.InlineKeyboardButton(text='Основная инфа', callback_data='menu_osninfo')
    btn_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='menu_info', row_width=1)
    btn_menu_lf = types.InlineKeyboardButton(text='Схема лофта', callback_data='menu_loft')
    btn_menu_pravila = types.InlineKeyboardButton(text='Правила', callback_data='menu_pravila')
    pagination.add(previous_button, btn_menu, next_button, btn_menu_osninfo, btn_menu_lf, btn_menu_pravila)
    bot.send_photo(chat_id_2, photo=open(bar_dict[page - 1], 'rb'), caption=f"Страница {page} из {count}",
                   reply_markup=pagination)

def menu_pravila(chat_id_2, user_stat):
    pagination = types.InlineKeyboardMarkup()
    page = user_stat[str(chat_id_2)]["page_rules"]
    count = len(rules_dict)
    # добавляю кнопочки
    previous_button = types.InlineKeyboardButton('Назад', callback_data='prev_page_pr')
    next_button = types.InlineKeyboardButton('Вперед', callback_data='next_page_pr')
    btn_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='menu_info')
    btn_menu_osninfo = types.InlineKeyboardButton(text='Основная инфа', callback_data='menu_osninfo')
    btn_menu_lf = types.InlineKeyboardButton(text='Схема лофта', callback_data='menu_loft')
    btn_menu_bar = types.InlineKeyboardButton('Барная карта', callback_data='menu_bar')
    pagination.add(previous_button, btn_menu, next_button, btn_menu_osninfo, btn_menu_lf, btn_menu_bar)
    # вывожу фотку
    bot.send_photo(chat_id_2, photo=open(rules_dict[page - 1], 'rb'), caption=f"Страница {page} из {count}",
                   reply_markup=pagination)





def menu_osninfo(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_menu_osninfo = types.InlineKeyboardButton(text='Основная инфа', callback_data='menu_osninfo')
    btn_menu_pravila = types.InlineKeyboardButton(text='Правила', callback_data='menu_pravila')
    btn_menu_bar = types.InlineKeyboardButton(text='Барная карта', callback_data='menu_bar')
    btn_menu_lf = types.InlineKeyboardButton(text='Схема лофта', callback_data='menu_loft')
    btn_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='menu_info')
    keyboard.add(btn_menu, btn_menu_lf, btn_menu_bar, btn_menu_pravila, btn_menu_osninfo)
    bot.send_message(message.from_user.id,
                     text="Уважаемые коллеги!\n\nДоводим до вашего сведения первые вводные о предстоящем корпоративе: мероприятие пройдет *в ночь с 25 на 26 ноября*, формат одежды: *office classic* или *office casual*.\n\nБолее подробную информацию читайте по [ссылке](https://t.me/peachteamcommunity/130)",
                     reply_markup=keyboard, parse_mode="Markdown")

def razvodka_change_facultet(message):
    with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
        file_read = f.read()
        if file_read != '':
            words = json.loads(file_read)
        else:
            words = dict()
    if message.from_user.username in words:
        global data, kostyl,university,for_who, from_where
        try:
            data_list = str(data[message.from_user.id]).split() + ['-', '-', '-']
            with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
                file_read = f.read()
                if file_read != '':
                    words = json.loads(file_read)
                else:
                    words = dict()
                old_datetime = words[message.from_user.username][7]
                words[message.from_user.username] = [message.from_user.id, data_list[0], data_list[1], data_list[2], university[message.from_user.id], for_where, for_who, old_datetime]
            with open('/home/romanloqi/code/guests_ns.json', 'w', encoding='UTF-8') as f:
                json.dump(words, f)
                print(words[message.from_user.username])
        except KeyError:
            pass
        keyboard = types.InlineKeyboardMarkup()
        btn_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu_da')
        keyboard.add(btn_menu)
        bot.send_message(message.from_user.id,
                         text='Твой факультет изменен успешно!', reply_markup=keyboard)


    elif message.from_user.username not in words:
        buy_bilet_from_who(message)

def razvodka_change_from_who(message):
    with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
        file_read = f.read()
        if file_read != '':
            words = json.loads(file_read)
        else:
            words = dict()
    if message.from_user.username in words:
        global data, kostyl,university,for_who, from_where
        try:
            data_list = str(data[message.from_user.id]).split() + ['-', '-', '-']
            with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
                file_read = f.read()
                if file_read != '':
                    words = json.loads(file_read)
                else:
                    words = dict()
                old_datetime = words[message.from_user.username][7]
                words[message.from_user.username] = [message.from_user.id, data_list[0], data_list[1], data_list[2], university[message.from_user.id], for_where, for_who, old_datetime]
            with open('/home/romanloqi/code/guests_ns.json', 'w', encoding='UTF-8') as f:
                json.dump(words, f)
                print(words[message.from_user.username])
        except KeyError:
            pass
        keyboard = types.InlineKeyboardMarkup()
        btn_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu_da')
        keyboard.add(btn_menu)
        bot.send_message(message.from_user.id,
                         text='Информация изменена успешно!', reply_markup=keyboard)


    elif message.from_user.username not in words:
        buy_bilet_group_proverka(message)



def vozvrat(message):
    data[message.from_user.id]=""
    university[message.from_user.id]=""
    msg = bot.send_message(message.from_user.id, 'Введи свое ФИО заново')
    bot.register_next_step_handler(msg, buy_bilet_data)

def priem_data(message):
    global data, kostyl,university,for_who, from_where
    try:
        data_list = str(data[message.from_user.id]).split() + ['-', '-', '-']
        tz=pytz.timezone('Europe/Moscow')
        current_datetime = datetime.now(tz).isoformat(sep='T', timespec='seconds')
        with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
            file_read = f.read()
            if file_read != '':
                words = json.loads(file_read)
            else:
                words = dict()
        if message.from_user.username in words and data_list[:3] != ['0', '-', '-']:
            old_datetime = words[message.from_user.username][7]
            words[message.from_user.username] = [message.from_user.id, data_list[0], data_list[1], data_list[2], university[message.from_user.id], for_where, for_who, old_datetime]
        elif message.from_user.username not in words:
            words[message.from_user.username] = [message.from_user.id, data_list[0], data_list[1], data_list[2], university[message.from_user.id], for_where, for_who, current_datetime]
    #words[message.from_user.username] = [message.from_user.id, data_list[0], data_list[1], data_list[2], group[message.from_user.id]]
        with open('/home/romanloqi/code/guests_ns.json', 'w', encoding='UTF-8') as f:
            json.dump(words, f)
            print(words[message.from_user.username])
    except KeyError:
        pass

    keyboard = types.InlineKeyboardMarkup()
    btn_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu_da')
    keyboard.add(btn_menu)
    bot.send_message(message.from_user.id,
                         text='Поздравляем! Добавили в твой календарь событие "Корпоратив"!\n\nНа данном этапе ты можешь вернуться в главное меню.', reply_markup=keyboard)


def change_fio_kostyl(message):
    a = bot.send_message(message.from_user.id,text='Введи свое ФИО заново')
    bot.register_next_step_handler(a, change_fio)

def change_university_kostyl(message):
    a = bot.send_message(message.from_user.id,text='Введи свой ВУЗ заново')
    bot.register_next_step_handler(a, change_university)

def change_facultet_kostyl(message):
    change_facultet(message)

def change_from_who_kostyl(message):
    change_from_who(message)

def change_another_kostyl(message):
    change_another(message)



def change_data(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_friends = types.InlineKeyboardButton(text='Свое ФИО', callback_data='change_fio', one_time_keyboard=True)
    keyboard.add(btn_friends)
    btn_odnogroup = types.InlineKeyboardButton(text='ВУЗ', callback_data='change_university', one_time_keyboard=True)
    keyboard.add(btn_odnogroup)
    btn_social = types.InlineKeyboardButton(text='Факультет', callback_data='change_facultet', one_time_keyboard=True)
    keyboard.add(btn_social)
    btn_posvat = types.InlineKeyboardButton(text='Откуда узнал о тусовке «Ночь Социолога»', callback_data='change_from_who', one_time_keyboard=True)
    keyboard.add(btn_posvat)
    btn_another = types.InlineKeyboardButton(text='Случайно нажал/не хочу изменять', callback_data='change_another', one_time_keyboard=True)
    keyboard.add(btn_another)

    bot.send_message(message.from_user.id,
                            text='Выбери то, что желаешь изменить!', reply_markup=keyboard)

def change_fio(message): #Проверка на тип данных str
    global data, kostyl,university,for_who, from_where
    if isinstance(message.text, str):
        try:
            data[message.from_user.id] = message.text

            if len(message.text.split())<3:

                for i in range(3-len(message.text.split())):
                    data[message.from_user.id]+=" -"
            data_list = str(data[message.from_user.id]).split() + ['-', '-', '-']
            with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
                file_read = f.read()
                if file_read != '':
                    words = json.loads(file_read)
                else:
                    words = dict()
                old_datetime = words[message.from_user.username][7]
                words[message.from_user.username] = [message.from_user.id, data_list[0], data_list[1], data_list[2], university[message.from_user.id], for_where, for_who, old_datetime]
            with open('/home/romanloqi/code/guests_ns.json', 'w', encoding='UTF-8') as f:
                json.dump(words, f)
                print(words[message.from_user.username])

        except KeyError:
            pass
        keyboard = types.InlineKeyboardMarkup()
        btn_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu_da')
        keyboard.add(btn_menu)
        bot.send_message(message.from_user.id,
                         text='Твое ФИО изменено успешно!', reply_markup=keyboard)

    else:
        a = bot.send_message(message.from_user.id, text="Пожалуйста, введите корректные данные :)", parse_mode="Markdown") #Можешь изменить текст, который будет присылаться юзеру при ошибочном вводе
        bot.register_next_step_handler(a, change_fio)


def change_university(message):
    global data, kostyl,university,for_who, from_where
    if isinstance(message.text, str):
        try:
            university[message.from_user.id] = message.text
            data_list = str(data[message.from_user.id]).split() + ['-', '-', '-']
            with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
                file_read = f.read()
                if file_read != '':
                    words = json.loads(file_read)
                else:
                    words = dict()
                old_datetime = words[message.from_user.username][7]
                words[message.from_user.username] = [message.from_user.id, data_list[0], data_list[1], data_list[2], university[message.from_user.id], for_where, for_who, old_datetime]
            with open('/home/romanloqi/code/guests_ns.json', 'w', encoding='UTF-8') as f:
                json.dump(words, f)
                print(words[message.from_user.username])
        except KeyError:
            pass
        keyboard = types.InlineKeyboardMarkup()
        btn_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu_da')
        keyboard.add(btn_menu)
        bot.send_message(message.from_user.id,
                         text='Твой ВУЗ изменен успешно!', reply_markup=keyboard)
    else:
        a = bot.send_message(message.from_user.id, text="Пожалуйста, введите корректные данные :)", parse_mode="Markdown") #Можешь изменить текст, который будет присылаться юзеру при ошибочном вводе
        bot.register_next_step_handler(a, change_university)

def change_facultet(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_social_studies = types.InlineKeyboardButton(text='Социальные науки', callback_data='social_studies',one_time_keyboard=True)
    keyboard.add(btn_social_studies)
    btn_computer_studies = types.InlineKeyboardButton(text='Компьютерные науки', callback_data='computer_studies',one_time_keyboard=True)
    keyboard.add(btn_computer_studies)
    btn_human_studies = types.InlineKeyboardButton(text='Гуманитарные науки', callback_data='human_studies',one_time_keyboard=True)
    keyboard.add(btn_human_studies)
    btn_natural_studies = types.InlineKeyboardButton(text='Естественные науки', callback_data='natural_studies', one_time_keyboard=True)
    keyboard.add(btn_natural_studies)
    btn_physical_studies = types.InlineKeyboardButton(text='Физические науки', callback_data='physical_studies', one_time_keyboard=True)
    keyboard.add(btn_physical_studies)
    btn_another_studies = types.InlineKeyboardButton(text='Другое/не учусь в вузе', callback_data='another_studies', one_time_keyboard=True)
    keyboard.add(btn_another_studies)

    bot.send_message(message.from_user.id,
                            text='Выбери заново, с какого ты факультета!', reply_markup=keyboard)

def change_from_who(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_friends = types.InlineKeyboardButton(text='От друзей', callback_data='friends', one_time_keyboard=True)
    keyboard.add(btn_friends)
    btn_odnogroup = types.InlineKeyboardButton(text='От одногруппников/однокурсников', callback_data='odnogroup', one_time_keyboard=True)
    keyboard.add(btn_odnogroup)
    btn_social = types.InlineKeyboardButton(text='Из соцсетей', callback_data='social', one_time_keyboard=True)
    keyboard.add(btn_social)
    btn_posvat = types.InlineKeyboardButton(text='Пришел/ла с посвята', callback_data='posvat', one_time_keyboard=True)
    keyboard.add(btn_posvat)
    btn_another = types.InlineKeyboardButton(text='Другое', callback_data='another', one_time_keyboard=True)
    keyboard.add(btn_another)

    bot.send_message(message.from_user.id,
                            text='Выбери заново, откуда ты узнал/ла о Ночи Социолога!', reply_markup=keyboard)

def change_another(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu_da')
    keyboard.add(btn_menu)
    bot.send_message(message.from_user.id,
                         text='Информация изменена успешно!', reply_markup=keyboard)



def buy_bilet_group_proverka(message):

    keyboard = types.InlineKeyboardMarkup()
    btn_da = types.InlineKeyboardButton(text='Да', callback_data='da', one_time_keyboard=True)
    keyboard.add(btn_da)
    btn_net = types.InlineKeyboardButton(text='Нет', callback_data='net',one_time_keyboard=True)
    keyboard.add(btn_net)
    bot.send_message(message.from_user.id,
                            text='Спасибо! А теперь проверь, всё ли введено верно: Ты — ' + data[message.from_user.id] + ' обучаешься в ' + university[message.from_user.id] + '?' ' Нажми «да», если все верно, и «нет» — если нужно перезаписать данные.\n\n*ВАЖНО — НЕ ЗАБУДЬ НАЖАТЬ НА КНОПКУ «ДА» ЕСЛИ ВСЕ ВЕРНО*, иначе твои данные не будут записаны.', reply_markup=keyboard, parse_mode="Markdown")



def buy_bilet_from_who(message):

    keyboard = types.InlineKeyboardMarkup()
    btn_friends = types.InlineKeyboardButton(text='От друзей', callback_data='friends', one_time_keyboard=True)
    keyboard.add(btn_friends)
    btn_odnogroup = types.InlineKeyboardButton(text='От одногруппников/однокурсников', callback_data='odnogroup', one_time_keyboard=True)
    keyboard.add(btn_odnogroup)
    btn_social = types.InlineKeyboardButton(text='Из соцсетей', callback_data='social', one_time_keyboard=True)
    keyboard.add(btn_social)
    btn_posvat = types.InlineKeyboardButton(text='Пришел/а с посвята', callback_data='posvat', one_time_keyboard=True)
    keyboard.add(btn_posvat)
    btn_another = types.InlineKeyboardButton(text='Другое', callback_data='another', one_time_keyboard=True)
    keyboard.add(btn_another)

    bot.send_message(message.from_user.id,
                            text='Откуда ты узнал/ла о тусовке «Ночь социолога?»', reply_markup=keyboard)




def buy_bilet_from_where(message):

    keyboard = types.InlineKeyboardMarkup()
    btn_social_studies = types.InlineKeyboardButton(text='Социальные науки', callback_data='social_studies',one_time_keyboard=True)
    keyboard.add(btn_social_studies)
    btn_computer_studies = types.InlineKeyboardButton(text='Компьютерные науки', callback_data='computer_studies',one_time_keyboard=True)
    keyboard.add(btn_computer_studies)
    btn_human_studies = types.InlineKeyboardButton(text='Гуманитарные науки', callback_data='human_studies',one_time_keyboard=True)
    keyboard.add(btn_human_studies)
    btn_natural_studies = types.InlineKeyboardButton(text='Естественные науки', callback_data='natural_studies', one_time_keyboard=True)
    keyboard.add(btn_natural_studies)
    btn_physical_studies = types.InlineKeyboardButton(text='Физические науки', callback_data='physical_studies', one_time_keyboard=True)
    keyboard.add(btn_physical_studies)
    btn_another_studies = types.InlineKeyboardButton(text='Другое/не учусь в вузе', callback_data='another_studies', one_time_keyboard=True)
    keyboard.add(btn_another_studies)

    bot.send_message(message.from_user.id,
                            text='На каком факультете ты учишься?', reply_markup=keyboard)




def proverka_group(message):
    if isinstance(message.text, str): #Проверка на тип данных str
        global university
        university[message.from_user.id] = message.text
        buy_bilet_from_where(message)
    else:
        a = bot.send_message(message.from_user.id, text="Пожалуйста, введите корректные данные :)", parse_mode="Markdown") #Можешь изменить текст, который будет присылаться юзеру при ошибочном вводе
        bot.register_next_step_handler(a, proverka_group)


def buy_bilet_data(message):
    if isinstance(message.text, str): #Проверка на тип данных str
        global data
        data[message.from_user.id] = message.text

        if len(message.text.split())<3:

            for i in range(3-len(message.text.split())):
                data[message.from_user.id]+=" -"

        msg = bot.send_message(message.from_user.id, 'Напиши, из какого ты ВУЗа.\n\nЕсли ты не учишься в ВУЗе, то напиши «Нигде»')
        bot.register_next_step_handler(msg, proverka_group)
    else:
        a = bot.send_message(message.from_user.id, text="Пожалуйста, введите корректные данные :)", parse_mode="Markdown") #Можешь изменить текст, который будет присылаться юзеру при ошибочном вводе
        bot.register_next_step_handler(a, buy_bilet_data)


def buy_bilet(message):
    a = bot.send_message(message.from_user.id, text=text_oplata, parse_mode="Markdown")
    bot.register_next_step_handler(a, buy_bilet_data)

def check_oplata(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu_oplata')
    keyboard.add(btn_menu)

    with open('/home/romanloqi/code/guests_valid_ns(2).json', 'r', encoding='UTF-8') as f:
        file_read = f.read()
        words = json.loads(file_read)

    if message.from_user.username in words:
        words[message.from_user.username] += 1
        with open('/home/romanloqi/code/guests_valid_ns(2).json', 'w', encoding='UTF-8') as f:
            json.dump(words, f)
        bot.send_message(message.from_user.id,
                         text="Твоя оплата подтверждена. До встречи на корпоративе!", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,
                        text = "Тебя нет в списках... Если ты покупал билет, напиши @roman_khamrin", reply_markup=keyboard)


def get_info(message):
    keyboard = types.InlineKeyboardMarkup()
    btn_menu_osninfo = types.InlineKeyboardButton(text='Основная инфа', callback_data='menu_osninfo')
    btn_menu_pravila = types.InlineKeyboardButton(text='Правила', callback_data='menu_pravila')
    btn_menu_bar = types.InlineKeyboardButton(text='Барная карта', callback_data='menu_bar')
    btn_menu_lf = types.InlineKeyboardButton(text='Схема лофта', callback_data='menu_loft')
    btn_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='menu_info')
    keyboard.add(btn_menu, btn_menu_lf, btn_menu_bar, btn_menu_pravila, btn_menu_osninfo)
    bot.send_message(message.from_user.id,
                         text="Коллега, выбери информацию, которую желаешь узнать!", reply_markup=keyboard)




@bot.message_handler(commands=[ 'start' ])
def start(message):
    if isinstance(message, telebot.types.Message):
        with open('/home/romanloqi/code/guest_page.json', 'r') as f:
            user_stat = json.load(f)
            user_stat[str(message.chat.id)] = {"page_bar": 1, "page_rules": 1}
            with open ('/home/romanloqi/code/guest_page.json', 'w') as of:
                json.dump(user_stat, of)
    tz0 = pytz.timezone('Europe/Moscow')
    current_datetime0 = datetime.now(tz0).isoformat(sep='T', timespec='seconds')
    with open('/home/romanloqi/code/guests_start_ns.json', 'r', encoding='UTF-8') as f:
        file_read = f.read()
        if file_read != '':
            words = json.loads(file_read)
        else:
            words = dict()
    words[message.from_user.username] = [message.from_user.id, current_datetime0]
    with open('/home/romanloqi/code/guests_start_ns.json', 'w', encoding='UTF-8') as f:
        json.dump(words, f)
        print(words[message.from_user.username])
    with open('/home/romanloqi/code/guests_ns.json', 'r', encoding='UTF-8') as f:
        file_read = f.read()
        if file_read != '':
            words = json.loads(file_read)
        else:
            words = dict()
    if message.from_user.username in words:
        keyboard = types.InlineKeyboardMarkup()
        btn_reg = types.InlineKeyboardButton(text='Изменить данные', callback_data='change_data', one_time_keyboard=True)
        keyboard.add(btn_reg)
        btn_oplata = types.InlineKeyboardButton(text='Подтверждение оплаты', callback_data='oplata', one_time_keyboard=True)
        keyboard.add(btn_oplata)
        btn_info = types.InlineKeyboardButton(text='Информация о мероприятии', callback_data='info', one_time_keyboard=True)
        keyboard.add(btn_info)
        bot.send_message(message.from_user.id,
                         text=f"Добро пожаловать в меню для регистрации на Ночь Социолога, {message.from_user.first_name}!\n\nВыбери информацию, которую желаешь узнать.".format(
                             message.from_user), reply_markup=keyboard)

    elif message.from_user.username not in words:
        keyboard = types.InlineKeyboardMarkup()
        btn_reg = types.InlineKeyboardButton(text='Купить билет', callback_data='bilet', one_time_keyboard=True)
        keyboard.add(btn_reg)
        btn_oplata = types.InlineKeyboardButton(text='Подтверждение оплаты', callback_data='oplata', one_time_keyboard=True)
        keyboard.add(btn_oplata)
        btn_info = types.InlineKeyboardButton(text='Информация о мероприятии', callback_data='info', one_time_keyboard=True)
        keyboard.add(btn_info)
        bot.send_message(message.from_user.id,
                         text=f"Добро пожаловать в меню для регистрации на Ночь Социолога, {message.from_user.first_name}!\n\nВыбери информацию, которую желаешь узнать.\n\nКонтакты техподдержки в шапке бота!".format(
                             message.from_user), reply_markup=keyboard)






bot.polling(none_stop=True)