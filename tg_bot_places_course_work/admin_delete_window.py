from telebot import types

from functions import *


def delete_place_function(message):
    try:

        there_is_admin = True if get_admin_something(message, 'Count(adminID)') == 1 else False

        if there_is_admin:

            select_place_name(message)
            new_message = bot.reply_to(message, "Введите правильное название места из списка ваших добавленных мест")
            bot.register_next_step_handler(new_message, delete_next_function, '')

        else:

            print("{} trying to use delete admin functions".format(message.chat.username))
            start_window(message)

    except Exception as e:
        print("ERROR {} delete_place_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: delete_place_function')


def delete_next_function(message, name):
    try:

        req = "SELECT Count(placeName) FROM Place WHERE placeName = %s"
        req_val = (message.text,)
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        there_is_place = True if my_result[0][0] == 1 else False

        if there_is_place == 0:
            bot.send_message(message.chat.id, 'Такого места нет')
            return start_window(message)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        item1 = types.KeyboardButton("Кухня")
        item2 = types.KeyboardButton("Метро")
        item3 = types.KeyboardButton("Адрес")
        item4 = types.KeyboardButton("Атмосфера")
        item5 = types.KeyboardButton("Формат")
        item6 = types.KeyboardButton("Досуг")
        item7 = types.KeyboardButton("Подходит для")
        item8 = types.KeyboardButton("Удалить место полностью")
        item9 = types.KeyboardButton("Предварительный просмотр")
        item10 = types.KeyboardButton("Готово")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        if name == '':

            new_message = bot.reply_to(message, 'Выберите что необходимо удалить в ' + message.text,
                                       reply_markup=markup)
            bot.register_next_step_handler(new_message, case_delete_function, message.text)

        else:

            new_message = bot.reply_to(message, 'Выберите что необходимо удалить в ' + name,
                                       reply_markup=markup)
            bot.register_next_step_handler(new_message, case_delete_function, name)

    except Exception as e:
        print("ERROR {} delete_next_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: delete_next_function')


def case_delete_function(message, name):
    try:

        if message.text == "Кухня":

            new_message = bot.reply_to(message, 'Введите название кухни')
            bot.register_next_step_handler(new_message, delete_atribute_function,
                                           name, 'cuisineID', 'cuisineName',
                                           'PlaceCuisinesView', 'PlaceCuisines')
        elif message.text == "Метро":

            new_message = bot.reply_to(message, 'Введите название метро')
            bot.register_next_step_handler(new_message, delete_atribute_function,
                                           name, 'metroID', 'metroName',
                                           'PlaceMetrosView', 'PlaceMetros')
        elif message.text == "Адрес":

            new_message = bot.reply_to(message, 'Введите адрес')
            bot.register_next_step_handler(new_message, delete_atribute_function,
                                           name, 'addressID', 'addressName',
                                           'PlaceAddressesView', 'PlaceAddresses')
        elif message.text == "Атмосфера":

            new_message = bot.reply_to(message, 'Введите название атмосферы')
            bot.register_next_step_handler(new_message, delete_atribute_function,
                                           name, 'atmosphereID', 'atmosphereName',
                                           'PlaceAtmospheresView', 'PlaceAtmospheres')
        elif message.text == "Формат":

            new_message = bot.reply_to(message, 'Введите название формата')
            bot.register_next_step_handler(new_message, delete_atribute_function,
                                           name, 'formatID', 'formatName',
                                           'PlaceFormatsView', 'PlaceFormats')
        elif message.text == "Досуг":

            new_message = bot.reply_to(message, 'Введите название досуга')
            bot.register_next_step_handler(new_message, delete_atribute_function,
                                           name, 'leisureID', 'leisureName',
                                           'PlaceLeisuresView', 'PlaceLeisures')
        elif message.text == "Подходит для":

            new_message = bot.reply_to(message, 'Введите для чего подходит')
            bot.register_next_step_handler(new_message, delete_atribute_function,
                                           name, 'fitID', 'fitName',
                                           'PlaceFitsView', 'PlaceFits')
        elif message.text == "Предварительный просмотр":

            bot.send_message(message.chat.id, 'Ваше место:')
            prepare_view_function(message, name, delete_next_function)

        elif message.text == "Удалить место полностью":

            delete_place_by_name_function(message, name)

        elif message.text == "Готово":

            start_window_admin(message)

    except Exception as e:
        print("ERROR {} case_delete_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: case_delete_function')


def delete_atribute_function(message, name, atr_ID, atr_name, atr_view, atr_relation):
    try:

        req = "SELECT {}, placeID FROM {} WHERE {} = %s and placeName = %s".format(atr_ID, atr_view, atr_name)
        req_val = (message.text, name, )
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        if len(my_result) == 0:

            bot.send_message(message.chat.id, "Вы ввели атрибут неправильно: {}, либо что-то пошло не так".format(message.text))
            delete_next_function(message, name)

        else:

            my_atrID = my_result[0]
            req = "DELETE FROM {} WHERE {} = {} AND placeID = {}".format(atr_relation, atr_ID, my_atrID[0], my_atrID[1])
            cursor.execute(req)
            mydb.commit()

            print("{} delete relation {}: {} - {} and {} - {}".format(message.chat.username,
                                                                      atr_relation, atr_ID,
                                                                      my_atrID[0], 'placeID', my_atrID[1]))

            bot.send_message(message.chat.id, "Атрибут: \"{}\" успешно удален из: {}".format(message.text, name))
            delete_next_function(message, name)

    except Exception as e:
        print("ERROR {} delete_atribute_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: delete_atribute_function')


def delete_place_by_name_function(message, name):
    try:

        sql = "DELETE FROM Place WHERE placeName = %s"
        val = (name, )
        cursor.execute(sql, val)
        mydb.commit()

        print("{} delete Place: {}".format(message.chat.username, name))

        bot.send_message(message.chat.id, "Место успешно удалено")
        delete_next_function(message, name)

    except Exception as e:
        print("ERROR {} delete_place_by_name_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: delete_place_by_name_function')

