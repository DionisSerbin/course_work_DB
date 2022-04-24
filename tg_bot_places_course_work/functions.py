from telebot import types

from start_window import *


def create_place_markup():
    try:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        item2 = types.KeyboardButton("Средний чек")
        item3 = types.KeyboardButton("Кухня")
        item4 = types.KeyboardButton("Метро")
        item5 = types.KeyboardButton("Адрес")
        item6 = types.KeyboardButton("Атмосфера")
        item7 = types.KeyboardButton("Формат")
        item8 = types.KeyboardButton("Dog-friendly")
        item9 = types.KeyboardButton("Досуг")
        item10 = types.KeyboardButton("Подходит для")
        item11 = types.KeyboardButton("Описание")
        item12 = types.KeyboardButton("Ссылка")
        item13 = types.KeyboardButton("Фото")
        item1 = types.KeyboardButton("Предварительный просмотр")
        item14 = types.KeyboardButton("Готово")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
                   item14, item1)
        return markup

    except Exception as e:
        print("ERROR: create_place_markup")


def select_place_name(message):
    try:

        req = "SELECT placeName FROM Place WHERE adminID in (SELECT adminID FROM Admin WHERE adminName = %s)"
        req_val = (message.chat.username,)
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        text = ""
        for x in my_result:
            if x[0] is not None:
                text += " " + x[0] + "\n"

        bot.send_message(message.chat.id, text)

    except Exception as e:
        print("ERROR {} select_place_name".format(message.chat.username))
        bot.reply_to(message, 'oooops: select_place_name')


def case_place_function(message, name, func):
    try:

        if message.text == "Средний чек":

            new_message = bot.reply_to(message, 'Введите средний чек')
            bot.register_next_step_handler(new_message, update_one_attribute,
                                           name, message.text, func)
        elif message.text == "Кухня":

            new_message = bot.reply_to(message, 'Введите название кухни')
            bot.register_next_step_handler(new_message, update_many_atribute_function,
                                           name, message.text, func)
        elif message.text == "Метро":

            new_message = bot.reply_to(message, 'Введите название метро')
            bot.register_next_step_handler(new_message, update_many_atribute_function,
                                           name, message.text, func)
        elif message.text == "Адрес":

            new_message = bot.reply_to(message, 'Введите адрес')
            bot.register_next_step_handler(new_message, update_many_atribute_function,
                                           name, message.text, func)
        elif message.text == "Атмосфера":

            new_message = bot.reply_to(message, 'Введите название атмосферы')
            bot.register_next_step_handler(new_message, update_many_atribute_function,
                                           name, message.text, func)
        elif message.text == "Формат":

            new_message = bot.reply_to(message, 'Введите название формата')
            bot.register_next_step_handler(new_message, update_many_atribute_function,
                                           name, message.text, func)
        elif message.text == "Dog-friendly":

            new_message = bot.reply_to(message, 'Введите да или нет')
            bot.register_next_step_handler(new_message, update_one_attribute,
                                           name, message.text, func)
        elif message.text == "Досуг":

            new_message = bot.reply_to(message, 'Введите название досуга')
            bot.register_next_step_handler(new_message, update_many_atribute_function,
                                           name, message.text, func)
        elif message.text == "Подходит для":

            new_message = bot.reply_to(message, 'Введите для чего подходит')
            bot.register_next_step_handler(new_message, update_many_atribute_function,
                                           name, message.text, func)
        elif message.text == "Описание":

            new_message = bot.reply_to(message, 'Введите описание')
            bot.register_next_step_handler(new_message, update_one_attribute,
                                           name, message.text, func)
        elif message.text == "Ссылка":

            new_message = bot.reply_to(message, 'Введите ссылку')
            bot.register_next_step_handler(new_message, update_one_attribute,
                                           name, message.text, func)
        elif message.text == "Фото":

            new_message = bot.reply_to(message, 'Прикрепите фото')
            bot.register_next_step_handler(new_message, update_photo_function, name, func)

        elif message.text == "Предварительный просмотр":

            bot.send_message(message.chat.id, 'Ваше место:')
            prepare_view_function(message, name, func)

        elif message.text == "Готово":

            start_window_admin(message)

        else:

            bot.send_message(message.chat.id, 'Вы ввели что-то не так, попробуйте снова')
            func(message, name)

    except Exception as e:
        print("ERROR {} case_place_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: case_place_function')


def update_many_atribute_function(message, name, atr, func):
    atrName = tableName = relationName = atrNameID = ''
    try:

        if atr == "Кухня":

            atrName = 'cuisineName'
            tableName = 'Cuisine'
            relationName = 'PlaceCuisines'
            atrNameID = 'cuisineID'

        elif atr == "Метро":

            atrName = 'metroName'
            tableName = 'Metro'
            relationName = 'PlaceMetros'
            atrNameID = 'metroID'

        elif atr == "Адрес":

            atrName = 'addressName'
            tableName = 'Address'
            relationName = 'PlaceAddresses'
            atrNameID = 'addressID'

        elif atr == "Атмосфера":

            atrName = 'atmosphereName'
            tableName = 'Atmosphere'
            relationName = 'PlaceAtmospheres'
            atrNameID = 'atmosphereID'

        elif atr == "Формат":

            atrName = 'formatName'
            tableName = 'Format'
            relationName = 'PlaceFormats'
            atrNameID = 'formatID'

        elif atr == "Досуг":

            atrName = 'leisureName'
            tableName = 'Leisure'
            relationName = 'PlaceLeisures'
            atrNameID = 'leisureID'

        elif atr == "Подходит для":

            atrName = 'fitName'
            tableName = 'Fit'
            relationName = 'PlaceFits'
            atrNameID = 'fitID'

        req = "SELECT Count({}) FROM {} WHERE {} = %s".format(atrName, tableName, atrName)
        req_val = (message.text,)
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        there_is = True if my_result[0][0] == 1 else False

        if not there_is:
            sql = "INSERT INTO {} ({}) VALUE (%s)".format(tableName, atrName)
            val = (message.text,)
            cursor.execute(sql, val)
            mydb.commit()

        req = "SELECT {} FROM {} WHERE {} = %s".format(atrNameID, tableName, atrName)
        req_val = (message.text,)
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        atrID = int(my_result[0][0])

        sql = "INSERT INTO {} ({}, placeID) VALUES ({}, (SELECT placeID FROM Place WHERE  placeName = %s))" \
            .format(relationName, atrNameID, atrID)
        val = (name,)
        cursor.execute(sql, val)
        mydb.commit()

        func(message, name)

    except Exception as e:
        print("ERROR {} update_many_atribute_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: update_many_atribute_function')


def prepare_select_function(message, name, markup):
    try:

        req = "SELECT * FROM Place WHERE placeName = %s"
        req_val = (name,)
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        text = "<b>" + my_result[0][6] + "</b>"

        if my_result[0][1] is not None:

            text += "\n<b>Средний чек:</b> " + str(my_result[0][1])

        if my_result[0][5] is not None:

            text += "\n" + my_result[0][5]

        if my_result[0][4] is not None:

            text += "\n<b>Ссылка:</b> " + my_result[0][4]

        if my_result[0][2] is not None:

            if my_result[0][2] == 1:

                text += "\n<b>Dog-friendly:</b> Да"

            else:

                text += "\n<b>Dog-friendly:</b> Нет"

        text += select_many_atribute_function(name=name, atrName="cuisineName",
                                              atrView="PlaceCuisinesView", atrWord="Кухня")

        text += select_many_atribute_function(name=name, atrName="metroName",
                                              atrView="PlaceMetrosView", atrWord="Метро")

        text += select_many_atribute_function(name=name, atrName="addressName",
                                              atrView="PlaceAddressesView", atrWord="Адрес")

        text += select_many_atribute_function(name=name, atrName="atmosphereName",
                                              atrView="PlaceAtmospheresView", atrWord="Атмосфера")

        text += select_many_atribute_function(name=name, atrName="formatName",
                                              atrView="PlaceFormatsView", atrWord="Формат")

        text += select_many_atribute_function(name=name, atrName="leisureName",
                                              atrView="PlaceLeisuresView", atrWord="Досуг")

        text += select_many_atribute_function(name=name, atrName="fitName",
                                              atrView="PlaceFitsView", atrWord="Подходит для")

        if my_result[0][3] is not None:

            new_file = open(my_result[0][3], 'rb')

            if markup is not None:

                bot.send_photo(message.chat.id, photo=new_file, caption=text, parse_mode="HTML", reply_markup=markup)

            else:

                bot.send_photo(message.chat.id, photo=new_file, caption=text, parse_mode="HTML")

        else:

            if markup is not None:

                bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)

            else:

                bot.send_message(message.chat.id, text, parse_mode="HTML")

    except Exception as e:
        print("ERROR {} prepare_select_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: prepare_select_function')


def prepare_view_function(message, name, func):
    try:

        prepare_select_function(message, name, None)
        func(message, name)

    except Exception as e:
        print("ERROR {} prepare_view_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: prepare_view_function')


def select_many_atribute_function(name, atrName, atrView, atrWord):
    try:

        req = "SELECT {} FROM {} WHERE placeName = %s".format(atrName, atrView)
        req_val = (name,)
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        checkText = text = "\n<b>{}:</b>".format(atrWord)

        for x in my_result:

            if x[0] is not None:
                text += " " + x[0] + ";"

        if text != checkText:
            text = text[:-1]

        return "" if text == checkText else text
    except Exception as e:
        print("ERROR: select_many_atribute_function")


def update_photo_function(message, name, func):
    try:

        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        new_file = open(path_photo_bot + file_info.file_path[7:], 'wb')
        new_file.write(downloaded_file)

        sql = "UPDATE Place set placePhoto = %s WHERE placeName = %s"
        val = (path_photo_bd + new_file.name, name,)
        cursor.execute(sql, val)
        mydb.commit()

        func(message, name)
    except Exception as e:
        print("ERROR {} update_photo_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: update_photo_function')


def update_one_attribute(message, name, atr, func):
    try:

        sql = ""
        val = ""
        # value = message.text
        if atr == "Средний чек":

            sql = "UPDATE Place set averageCheck = {} WHERE placeName = %s".format(int(message.text))
            val = (name,)

        elif atr == "Описание":

            sql = "UPDATE Place set placeDescription = %s WHERE placeName = %s"
            val = (message.text, name,)

        elif atr == "Dog-friendly":

            if message.text == "Да" or message.text == "да" or message.text == "ДА":
                sql = "UPDATE Place set placeDogFriendly = {} WHERE placeName = %s".format(bool(1))
                val = (name,)
            else:
                sql = "UPDATE Place set placeDogFriendly = {} WHERE placeName = %s".format(bool(0))
                val = (name,)

        elif atr == "Ссылка":

            sql = "UPDATE Place set placeURL = %s WHERE placeName = %s"
            val = (message.text, name,)

        cursor.execute(sql, val)
        mydb.commit()

        print("{} update {} from {}".format(message.chat.username, atr, name))

        func(message, name)

    except Exception as e:
        print("ERROR {} update_one_attribute".format(message.chat.username))
        bot.reply_to(message, 'oooops: update_one_attribute')