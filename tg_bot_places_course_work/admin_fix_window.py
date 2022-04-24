from functions import *


def fix_place_funtion(message):
    try:

        there_is_admin = True if get_admin_something(message, 'Count(adminID)') == 1 else False

        if there_is_admin:
            select_place_name(message)
            new_message = bot.reply_to(message, "Введите правильное название места из списка ваших добавленных мест")
            bot.register_next_step_handler(new_message, fix_next_place_function, '')

        else:
            start_window(message)
    except Exception as e:
        print("ERROR {} fix_place_funtion".format(message.chat.username))
        bot.reply_to(message, 'oooops: fix_place_funtion')


def fix_next_place_function(message, name):
    try:

        req = "SELECT Count(placeName) FROM Place WHERE placeName = %s"
        req_val = (message.text,)
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        there_is_place = True if my_result[0][0] == 1 else False

        if there_is_place == 0:
            bot.send_message(message.chat.id, 'Такого места нет')
            return start_window(message)

        markup = create_place_markup()

        if name == '':

            new_message = bot.reply_to(message, 'Добавьте оставшиеся критерии заведения ' + message.text,
                                       reply_markup=markup)
            bot.register_next_step_handler(new_message, case_place_function, message.text, fix_next_place_function)
        else:

            new_message = bot.reply_to(message, 'Добавьте оставшиеся критерии заведения ' + name,
                                       reply_markup=markup)
            bot.register_next_step_handler(new_message, case_place_function, name, fix_next_place_function)

    except Exception as e:
        print("ERROR {} fix_next_place_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: fix_next_place_function')





