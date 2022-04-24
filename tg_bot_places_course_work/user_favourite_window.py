from telebot import types

from functions import prepare_select_function
from init_structures import *
from start_window import start_window


def user_favourites_window(message):
    try:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Посмотреть закладки")
        item2 = types.KeyboardButton("Назад")
        markup.add(item1, item2)

        new_message = bot.reply_to(message, "Посмотрите закладки или вернитесь назад",
                                   reply_markup=markup)
        bot.register_next_step_handler(new_message, case_user_favourites_function)

    except Exception as e:
        print("ERROR {} user_favourites_window".format(message.chat.username))
        bot.reply_to(message, 'oooops: user_favourites_window')


def case_user_favourites_function(message):
    try:

        if message.text == "Посмотреть закладки":

            req = "SELECT placeName FROM UserFavouritesPlacesView WHERE userName = %s"
            req_val = (message.chat.username,)
            cursor.execute(req, req_val)
            my_result = cursor.fetchall()

            for placeName in my_result:

                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Удалить {} из закладок".format(placeName[0]),
                                                      callback_data="del {}".format(placeName[0])))

                prepare_select_function(message, placeName[0], markup)

            user_favourites_window(message)

        elif message.text == "Назад":

            start_window(message)

    except Exception as e:
        print("ERROR {} case_user_favourites_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: case_user_favourites_function')