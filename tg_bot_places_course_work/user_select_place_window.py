from functions import *
from user_markup import *


def select_place_by_user(message, reply_text, sql_cond):
    try:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        item1 = types.KeyboardButton("Средний чек")
        item2 = types.KeyboardButton("Кухня")
        item3 = types.KeyboardButton("Метро")
        item5 = types.KeyboardButton("Атмосфера")
        item6 = types.KeyboardButton("Формат")
        item7 = types.KeyboardButton("Dog-friendly")
        item8 = types.KeyboardButton("Досуг")
        item9 = types.KeyboardButton("Подходит для")
        item10 = types.KeyboardButton("Готово")
        item11 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item5, item6, item7, item8, item9, item10, item11)

        if reply_text == "" and sql_cond == "":

            new_message = bot.reply_to(message, "Давайте подберем подходящие для вас места, для этого задайте фильтры "
                                                "по которым мы выберим для вас места",
                                       reply_markup=markup)
            bot.register_next_step_handler(new_message, case_user_place_function,
                                           "По этим фильтрам мы подберем вам место:", "WHERE")
        else:

            new_message = bot.reply_to(message, "Продолжим настраивать ваши фильтры", reply_markup=markup)
            bot.register_next_step_handler(new_message, case_user_place_function,
                                           reply_text, sql_cond)
    except Exception as e:
        print("ERROR {} select_place_by_user".format(message.chat.username))
        bot.reply_to(message, 'oooops: select_place_by_user')


def case_user_place_function(message, reply_text, sql_cond):
    try:

        if message.text == "Средний чек":

            new_message = bot.reply_to(message, 'Введите число до какой суммы вам подходит средний чек')
            bot.register_next_step_handler(new_message, select_average_check,
                                           reply_text, sql_cond)
        elif message.text == "Кухня":

            select_many_atr(message, reply_text, sql_cond, True, 'cuisineName', 'Cuisine', 'Кухня',
                            'Выберите какие кухни вы хотите')

        elif message.text == "Метро":

            select_many_atr(message, reply_text, sql_cond, True, 'metroName', 'Metro', 'Метро',
                            'Выберите подходящие станции метро, которые вы хотите')

        elif message.text == "Атмосфера":

            select_many_atr(message, reply_text, sql_cond, True, 'atmosphereName', 'Atmosphere', 'Атмосфера',
                            'Выберите какую атмосферу вы хотите')

        elif message.text == "Формат":

            select_many_atr(message, reply_text, sql_cond, True, 'formatName', 'Format', 'Формат',
                            'Выберите какой формат места вы хотите')

        elif message.text == "Dog-friendly":

            new_message = bot.reply_to(message, 'Введите да или нет')
            bot.register_next_step_handler(new_message, select_dog_friendly,
                                           reply_text, sql_cond)
        elif message.text == "Досуг":

            select_many_atr(message, reply_text, sql_cond, True, 'leisureName', 'Leisure', 'Досуг',
                            'Выберите какой вариант досуга вы хотите')

        elif message.text == "Подходит для":

            select_many_atr(message, reply_text, sql_cond, True, 'fitName', 'Fit', 'Подходит для',
                            'Выберите для чего вы хотите подобрать место')

        elif message.text == "Готово":

            select_by_filters(message, reply_text, sql_cond)

        elif message.text == "Назад":

            start_window(message)

    except Exception as e:
        print("ERROR {} case_user_place_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: case_user_place_function')


def select_by_filters(message, reply_text, sql_cond):
    try:

        bot.send_message(message.chat.id, reply_text, parse_mode="HTML")

        if sql_cond == "WHERE":

            sql = "SELECT DISTINCT placeName FROM PlaceView WHERE true".format(sql_cond)

        else:

            sql = "SELECT DISTINCT placeName FROM PlaceView {}".format(sql_cond)

        cursor.execute(sql)
        my_result = cursor.fetchall()

        for placeName in my_result:

            print("{} select Place: {}".format(message.chat.username, placeName[0]))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Добавить {} в закладки".format(placeName[0]),
                                                  callback_data="fav {}".format(placeName[0])))

            prepare_select_function(message, placeName[0], markup)

        start_window_user(message)
    except Exception as e:
        print("ERROR {} select_by_filters".format(message.chat.username))
        bot.reply_to(message, 'oooops: select_by_filters')


def error_query(message):

    return message.text == "Кухня" or message.text == "Метро" or message.text == "Атмосфера" \
           or message.text == "Формат" or message.text == "Досуг" or message.text == "Подходит для" \
           or message.text == "Dog-friendly" or message.text == "Средний чек"


def select_average_check(message, reply_text, sql_cond):
    try:

        if error_query(message):

            bot.send_message(message.chat.id, 'Вы ввели что-то не так')
            return select_place_by_user(message, reply_text, sql_cond)

        reply_text += "\n<b>Средний чек (до):</b> {}".format(message.text)

        if sql_cond != "WHERE":

            sql_cond += " and averageCheck <= {}".format(message.text)

        else:

            sql_cond += " averageCheck <= {}".format(message.text)

        select_place_by_user(message, reply_text, sql_cond)

    except Exception as e:
        print("ERROR {} select_average_check".format(message.chat.username))
        bot.reply_to(message, 'oooops: select_average_check')


def select_dog_friendly(message, reply_text, sql_cond):
    try:

        if error_query(message):

            bot.send_message(message.chat.id, 'Вы ввели что-то не так')
            return select_place_by_user(message, reply_text, sql_cond)

        flag = False

        if message.text == "да":
            flag = True

        reply_text += "\n<b>Dog-friendly:</b> {}".format(message.text)

        if sql_cond != "WHERE":

            sql_cond += " and placeDogFriendly = {}".format(flag)

        else:

            sql_cond += " placeDogFriendly = {}".format(flag)

        select_place_by_user(message, reply_text, sql_cond)

    except Exception as e:
        print("ERROR {} select_dog_friendly".format(message.chat.username))
        bot.reply_to(message, 'oooops: select_dog_friendly')


def select_many_atr(message, reply_text, sql_cond, first_time, atr_name, atr_table, atr_word, text):
    try:

        markup = get_markup(atr_name, atr_table)
        new_message = bot.reply_to(message, text, reply_markup=markup)

        bot.register_next_step_handler(new_message, select_from_many_atr_next_func,
                                       reply_text, sql_cond, first_time, atr_name, atr_table, atr_word)

    except Exception as e:
        print("ERROR {} select_many_atr".format(message.chat.username))
        bot.reply_to(message, 'oooops: select_many_atr')


def select_from_many_atr_next_func(message, reply_text, sql_cond, first_time, atrName, atrTable, atrWord):
    try:

        if error_query(message):

            bot.send_message(message.chat.id, 'Вы ввели что-то не так')
            return select_place_by_user(message, reply_text, sql_cond)

        if message.text == "Готово":

            if not first_time:
                reply_text = reply_text[:-1]

            sql_cond += ')'

            select_place_by_user(message, reply_text, sql_cond)

        else:

            if not first_time:

                sql_cond += " or {} = \'{}\'".format(atrName, message.text)

            elif sql_cond != "WHERE":

                sql_cond += " and ({} = \'{}\'".format(atrName, message.text)

            else:

                sql_cond += " ({} = \'{}\'".format(atrName, message.text)

            if first_time:

                first_time = False
                reply_text += "\n<b>{}</b>:".format(atrWord)
                
            reply_text += " {};".format(message.text)

            select_many_atr(message, reply_text, sql_cond, first_time,
                            atrName, atrTable, atrWord, 'Продолжите подбор по фильтру: {}'.format(atrWord))

    except Exception as e:
        print("ERROR {} select_from_many_atr_next_func".format(message.chat.username))
        bot.reply_to(message, 'oooops: select_from_many_atr_next_func')
