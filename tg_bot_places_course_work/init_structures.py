import telebot
import mysql.connector

admin_login_key = 1337

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="my-secret-pw",
    port="3306",
    database="course_work"
)

cursor = mydb.cursor()


bot = telebot.TeleBot("5256330090:AAEj86lm7Y0zAXI2pKwjN1geNcAiQ7Gcn_c",
                      parse_mode=None)

path_photo_bot = "coursework_bd_photo/"

path_photo_bd = "/Users/denisserbin/PycharmProjects/tg_bot_places_course_work/"


def get_admin_something(message, id):
    try:

        req = "SELECT {} FROM Admin WHERE adminName = %s".format(id)
        req_val = (message.chat.username, )
        cursor.execute(req, req_val)
        my_result = cursor.fetchall()

        return my_result[0][0]

    except Exception as e:
        print("ERROR {} get_admin_something".format(message.chat.username))
        bot.reply_to(message, 'oooops: get_admin_something')
