from admin_add_window import *
from admin_fix_window import *
from admin_delete_window import *
from user_select_place_window import *
from user_favourite_window import *


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:

        bot.send_message(message.chat.id, "Привет ✌️ \n "
                                          "*Не знаешь куда сходить вкусно поесть и хорошо провести время?* \n "
                                          "Тогда я помогу тебе с выбором подходящего тебе места! \n\n"
                                          "Ты можешь войти в нашу систему и сохранять понравившиеся "
                                          "тебе места или просто подобрать место")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Начнем")
        markup.add(item1)

        bot.send_message(message.chat.id, 'Давай начнем', reply_markup=markup)

    except Exception as e:
        print("ERROR {} send_welcome".format(message.chat.username))
        bot.reply_to(message, 'oooops: send_welcome')


@bot.message_handler(commands=['button'])
def button_message(message):
    try:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Начнем")
        markup.add(item1)

        bot.send_message(message.chat.id, 'Давай начнем', reply_markup=markup)

    except Exception as e:
        print("ERROR {} button_message".format(message.chat.username))
        bot.reply_to(message, 'oooops: button_message')


@bot.message_handler(content_types='text')
def message_reply(message):

    try:

        if message.text == "Начнем" or message.text == "Начать заново" or message.text == "Начальное меню":

            start_window(message)

        elif message.text == "Подобрать место":

            select_place_by_user(message, "", "")

        elif message.text == "Мои закладки":

            user_favourites_window(message)

        elif message.text == "admin":

            register_admin_window(message)

        elif message.text == "Продолжить как пользователь":

            start_window_user(message)

        elif message.text == "Продолжить как администратор":

            start_window_admin(message)

        elif message.text == "Добавить почту":

            add_admin_mail(message)

        elif message.text == "Добавить место":

            add_place_function(message)

        elif message.text == "Редактировать место":

            fix_place_funtion(message)

        elif message.text == "Удалить что-то в месте":

            delete_place_function(message)

        req = "SELECT Count(adminName) FROM Admin WHERE adminName = %s"
        req_val = (message.chat.username,)
        cursor.execute(req, req_val)
        my_result_admin = cursor.fetchall()

        if not my_result_admin:
            bot.send_message(message.chat.id, "Неизвестная мне команда")

    except Exception as e:
        print("ERROR {} message_reply".format(message.chat.username))
        bot.reply_to(message, 'oooops: message_reply')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:

        call_data_split = call.data.split(" ", 1)

        if call_data_split[0] == "fav":

            sql = "SELECT count(placeID) FROM UserFavouritesPlacesView WHERE placeName = %s and userName = %s"
            sql_val = (call_data_split[1], call.from_user.username)
            cursor.execute(sql, sql_val)
            my_result = cursor.fetchall()

            there_is_place = True if my_result[0][0] == 1 else False

            if not there_is_place:

                user_req = "SELECT userID FROM User WHERE userName = %s"
                user_req_val = (call.from_user.username,)
                cursor.execute(user_req, user_req_val)
                user_result = cursor.fetchall()

                place_req = "SELECT placeID FROM Place WHERE placeName = %s"
                place_req_val = (call_data_split[1],)
                cursor.execute(place_req, place_req_val)
                place_result = cursor.fetchall()

                req = "INSERT INTO Favourite (userID, placeID) VALUES " \
                      "(%s, %s)"
                req_val = (user_result[0][0], place_result[0][0],)
                cursor.execute(req, req_val)
                mydb.commit()

                print("{} add {} in Favourites".format(call.from_user.username, call_data_split[1]))

                bot.answer_callback_query(call.id, "{} добавлено в закладки".format(call_data_split[1]))

            else:

                bot.answer_callback_query(call.id, "{} уже есть в закладках".format(call_data_split[1]))

        elif call_data_split[0] == "del":

            sql = "SELECT count(placeID) FROM UserFavouritesPlacesView WHERE placeName = %s and userName = %s"
            sql_val = (call_data_split[1], call.from_user.username)
            cursor.execute(sql, sql_val)
            my_result = cursor.fetchall()

            there_is_place = True if my_result[0][0] == 1 else False

            if there_is_place:

                req_view = "SELECT placeID, userID FROM UserFavouritesPlacesView WHERE placeName = %s and userName = %s"
                req_view_val = (call_data_split[1], call.from_user.username,)
                cursor.execute(req_view, req_view_val)
                view_result = cursor.fetchall()

                req = "DELETE FROM Favourite WHERE placeID = %s and userID = %s"
                req_val = (view_result[0][0], view_result[0][1],)
                cursor.execute(req, req_val)
                mydb.commit()

                print("{} delete {} from Favourites".format(call.from_user.username, call_data_split[1]))

                bot.answer_callback_query(call.id, "{} удалено из закладок".format(call_data_split[1]))

            else:

                bot.answer_callback_query(call.id, "{} уже удалено".format(call_data_split[1]))

    except Exception as e:
        print("ERROR {} callback_query".format(call.from_user.username))
        bot.answer_callback_query(call.id, 'oooops: callback_query')


if __name__ == '__main__':
    bot.polling(none_stop=True)
