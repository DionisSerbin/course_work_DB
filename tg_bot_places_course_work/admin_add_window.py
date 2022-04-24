from functions import *


def add_admin_mail(message):
    try:

        new_message = bot.reply_to(message, "Введите название почты")
        bot.register_next_step_handler(new_message, add_mail_function)

    except Exception as e:
        print("ERROR {} add_admin_mail".format(message.chat.username))
        bot.reply_to(message, 'oooops: add_admin_mail')


def add_mail_function(message):
    try:

        sql = "UPDATE Admin SET adminEmail = %s WHERE adminName = %s"
        val = (message.text, message.chat.username)
        cursor.execute(sql, val)
        mydb.commit()

        bot.send_message(message.chat.id, "Почта успешно добавлена")
        print("{} add mail {}".format(message.chat.username, message.text))
        start_window_admin(message)

    except Exception as e:
        print("ERROR {} add_mail_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: add_mail_function')


def add_place_function(message):
    try:

        there_is_admin = True if get_admin_something(message, 'Count(adminID)') == 1 else False

        if there_is_admin:

            new_message = bot.reply_to(message, "Введите название места")
            bot.register_next_step_handler(new_message, add_next_place_function, '')

        else:

            start_window(message)

    except Exception as e:
        print("ERROR {} add_place_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: add_place_function')


def add_next_place_function(message, place_name):
    try:

        markup = create_place_markup()

        if place_name == '':

            sql = "INSERT INTO Place (adminID, placeName) VALUES ((SELECT adminID FROM Admin WHERE adminName = %s), %s)"
            val = (message.chat.username, message.text)
            cursor.execute(sql, val)
            mydb.commit()

            print("{} add Place {}".format(message.chat.username, message.text))

            new_message = bot.reply_to(message, 'Добавьте критерии заведения ' + message.text, reply_markup=markup)
            bot.register_next_step_handler(new_message, case_place_function, message.text, add_next_place_function)

        else:

            new_message = bot.reply_to(message, 'Добавьте оставшиеся критерии заведения ' + place_name,
                                       reply_markup=markup)
            bot.register_next_step_handler(new_message, case_place_function, place_name, add_next_place_function)

    except Exception as e:
        print("ERROR {} add_next_place_function".format(message.chat.username))
        bot.reply_to(message, 'oooops: add_next_place_function')

