from telebot import types

from init_structures import *


def start_window(message):
    try:
        if message.chat.username is None:
            bot.send_message(message.chat.id, 'Чтобы пользоваться ботом вам нужно Имя пользователя\n'
                                              'Чтобы его добавить вам нужно: зайти в раздел Настройки/'
                                              'Нажать кнопку Изм./Добавить имя пользователя\n'
                                              'После этого перезапустите бот и тогда вы сможете им воспользоваться')
            return 1

        req = "SELECT COUNT(userName) FROM User WHERE userName = %s"
        req_val = (message.chat.username, )
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        there_is_user = True if my_result[0][0] == 1 else False
        there_is_admin = True if get_admin_something(message, 'Count(adminName)') == 1 else False

        if there_is_user and there_is_admin:

            start_window_admin_user(message)

        elif there_is_user:

            start_window_user(message)

        elif there_is_admin:

            start_window_admin(message)

        else:

            register_user_window(message)

    except Exception as e:
        print("ERROR {} start_window".format(message.chat.username))
        bot.reply_to(message, 'oooops: start_window')


def start_window_admin_user(message):
    try:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Продолжить как пользователь")
        item2 = types.KeyboardButton("Продолжить как администратор")
        markup.add(item1).add(item2)

        bot.send_message(message.chat.id, 'Выберите кем вы хотите продолжить', reply_markup=markup)

    except Exception as e:
        print("ERROR {} start_window_admin_user".format(message.chat.username))
        bot.reply_to(message, 'oooops: start_window_admin_user')


def start_window_user(message):
    try:

        there_is_admin = True if get_admin_something(message, 'Count(adminName)') == 1 else False

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Подобрать место")
        item2 = types.KeyboardButton("Мои закладки")

        if there_is_admin:

            item3 = types.KeyboardButton("Продолжить как администратор")
            markup.add(item1).add(item2).add(item3)

        else:

            markup.add(item1).add(item2)

        bot.send_message(message.chat.id, 'Выберите один из вариантов возможностей пользователя', reply_markup=markup)

    except Exception as e:
        print("ERROR {} start_window_user".format(message.chat.username))
        bot.reply_to(message, 'oooops: start_window_user')


def start_window_admin(message):
    try:

        req = "SELECT Count(userName) FROM User WHERE userName = %s"
        req_val = (message.chat.username, )
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        there_is_user = True if my_result[0][0] == 1 else False
        there_is_mail = True if get_admin_something(message, 'Count(adminEmail)') == 1 else False

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Добавить место")
        item2 = types.KeyboardButton("Редактировать место")
        item3 = types.KeyboardButton("Удалить что-то в месте")

        if not there_is_mail and not there_is_user:

            item4 = types.KeyboardButton("Зарегистрироваться как пользователь")
            item5 = types.KeyboardButton("Добавить почту")
            markup.add(item1).add(item2).add(item3).add(item4).add(item5)

        elif not there_is_mail:

            item5 = types.KeyboardButton("Добавить почту")
            item6 = types.KeyboardButton("Продолжить как пользователь")
            markup.add(item1).add(item2).add(item3).add(item5).add(item6)

        elif not there_is_user:

            item4 = types.KeyboardButton("Зарегистрироваться как пользователь")
            markup.add(item1).add(item2).add(item3).add(item4)

        else:

            item4 = types.KeyboardButton("Начальное меню")
            item5 = types.KeyboardButton("Продолжить как пользователь")
            markup.add(item1).add(item2).add(item3).add(item4).add(item5)

        bot.send_message(message.chat.id, 'Выберите один из вариантов возможностей администратора', reply_markup=markup)

    except Exception as e:
        print("ERROR {} start_window_admin".format(message.chat.username))
        bot.reply_to(message, 'oooops: start_window_admin')


def register_user_window(message):
    try:

        sql = "INSERT INTO User (userName) VALUES (%s)"
        val = (message.chat.username, )
        cursor.execute(sql, val)
        mydb.commit()

        print("{} register as User".format(message.chat.username))

        start_window(message)

    except Exception as e:
        print("ERROR {} register_user_window".format(message.chat.username))
        bot.reply_to(message, 'oooops: register_user_window')


def register_admin_window(message):
    try:

        new_message = bot.reply_to(message, "Введите ключ доступа администратора")
        bot.register_next_step_handler(new_message, register_verify_admin)

    except Exception as e:
        print("ERROR {} register_admin_window".format(message.chat.username))
        bot.reply_to(message, 'oooops: register_admin_window')


def register_verify_admin(message):
    try:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Продолжить как администратор")
        markup.add(item1)

        if admin_login_key == int(message.text):
            sql = "INSERT INTO Admin (adminName) VALUES (%s)"
            val = (message.chat.username,)
            cursor.execute(sql, val)
            mydb.commit()

            print("{} register as Admin".format(message.chat.username))

            bot.send_message(message.chat.id, "вы успешно зарегистрировались\n ", reply_markup=markup)

        else:

            bot.send_message(message.chat.id, "Вы ввели неправильный ключ администратора\n "
                                              "Попробуйте зарегистрироваться заново или начните заново",
                             reply_markup=markup)

    except Exception as e:
        print("ERROR {} register_verify_admin".format(message.chat.username))
        bot.reply_to(message, 'oooops: register_verify_admin')
