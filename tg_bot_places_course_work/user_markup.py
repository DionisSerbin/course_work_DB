from telebot import types

from init_structures import *


def get_markup_cuisine_types():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton("авторская")
    item2 = types.KeyboardButton("азиатская")
    item3 = types.KeyboardButton("американская")
    item4 = types.KeyboardButton("вьетнамская")
    item5 = types.KeyboardButton("грузинская")
    item6 = types.KeyboardButton("европейская")
    item7 = types.KeyboardButton("завтраки")
    item8 = types.KeyboardButton("итальянская")
    item9 = types.KeyboardButton("китайская")
    item10 = types.KeyboardButton("коктейли")
    item11 = types.KeyboardButton("кондитерская")
    item12 = types.KeyboardButton("корейская")
    item13 = types.KeyboardButton("кофе")
    item14 = types.KeyboardButton("мексиканская")
    item15 = types.KeyboardButton("многопрофильное заведение")
    item16 = types.KeyboardButton("морская")
    item17 = types.KeyboardButton("паназиатская")
    item18 = types.KeyboardButton("перекусы")
    item19 = types.KeyboardButton("смешанная")
    item20 = types.KeyboardButton("спешелти")
    item21 = types.KeyboardButton("средиземноморская")
    item22 = types.KeyboardButton("тайская")
    item23 = types.KeyboardButton("фьюжн")
    item24 = types.KeyboardButton("чай")
    item25 = types.KeyboardButton("японская")
    item26 = types.KeyboardButton("Готово")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
               item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26)
    return markup


def get_markup_metro_types():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton("Александровский сад")
    item2 = types.KeyboardButton("Арбатская")
    item3 = types.KeyboardButton("Баррикадная")
    item4 = types.KeyboardButton("Бауманская")
    item5 = types.KeyboardButton("Библиотека им. Ленина")
    item6 = types.KeyboardButton("Добрынинская")
    item7 = types.KeyboardButton("Китай-город")
    item8 = types.KeyboardButton("Кузнецкий мост")
    item9 = types.KeyboardButton("Лубянка")
    item10 = types.KeyboardButton("Международная")
    item11 = types.KeyboardButton("Молодежная")
    item12 = types.KeyboardButton("Новокузнецкая")
    item13 = types.KeyboardButton("Отрадная")
    item14 = types.KeyboardButton("Охотный Ряд")
    item15 = types.KeyboardButton("Парк культуры")
    item16 = types.KeyboardButton("Площадь Революции")
    item17 = types.KeyboardButton("Пушкинская")
    item18 = types.KeyboardButton("Савеловская")
    item19 = types.KeyboardButton("Серпуховская")
    item20 = types.KeyboardButton("Смоленская")
    item21 = types.KeyboardButton("Солнцево")
    item22 = types.KeyboardButton("Сретенский бульвар")
    item23 = types.KeyboardButton("Сухаревская")
    item24 = types.KeyboardButton("Таганская")
    item25 = types.KeyboardButton("Тверская")
    item26 = types.KeyboardButton("Театральная")
    item27 = types.KeyboardButton("Трубная")
    item28 = types.KeyboardButton("Тургеневская")
    item29 = types.KeyboardButton("Цветной бульвар")
    item30 = types.KeyboardButton("Чеховская")
    item31 = types.KeyboardButton("Чистые пруды")
    item32 = types.KeyboardButton("Готово")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
               item14, item15, item16, item17, item18, item19, item20, item21, item22, item23,
               item24, item25, item26, item27, item28, item29, item30, item31, item32)
    return markup


def get_markup_atmosphere_types():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton("андерграунд")
    item2 = types.KeyboardButton("веселая")
    item3 = types.KeyboardButton("городская")
    item4 = types.KeyboardButton("женственная")
    item5 = types.KeyboardButton("загородная")
    item6 = types.KeyboardButton("к-поп")
    item7 = types.KeyboardButton("киношная")
    item8 = types.KeyboardButton("летняя")
    item9 = types.KeyboardButton("молодежная")
    item10 = types.KeyboardButton("оживленная")
    item11 = types.KeyboardButton("рабочая")
    item12 = types.KeyboardButton("расслабленная")
    item13 = types.KeyboardButton("спокойная")
    item14 = types.KeyboardButton("тусовочная")
    item15 = types.KeyboardButton("утонченная")
    item16 = types.KeyboardButton("уютная")
    item17 = types.KeyboardButton("футуристичная")
    item18 = types.KeyboardButton("художественная")
    item19 = types.KeyboardButton("элитная")
    item20 = types.KeyboardButton("Готово")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
               item14, item15, item16, item17, item18, item19, item20)
    return markup


def get_markup_format_types():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton("антикафе")
    item2 = types.KeyboardButton("бар")
    item3 = types.KeyboardButton("бар-клуб")
    item4 = types.KeyboardButton("винотека")
    item5 = types.KeyboardButton("винный бар")
    item6 = types.KeyboardButton("гастропаб")
    item7 = types.KeyboardButton("кальянная")
    item8 = types.KeyboardButton("кафе")
    item9 = types.KeyboardButton("кафе-кондитерская")
    item10 = types.KeyboardButton("кафе-самообслуживание")
    item11 = types.KeyboardButton("кофейня")
    item12 = types.KeyboardButton("лаунж-бар")
    item13 = types.KeyboardButton("ресторан")
    item14 = types.KeyboardButton("ресторан авторской кухни")
    item15 = types.KeyboardButton("ресторан быстрого питания")
    item16 = types.KeyboardButton("фаст-фуд")
    item17 = types.KeyboardButton("фуд-корт")
    item18 = types.KeyboardButton("чайная")
    item19 = types.KeyboardButton("Готово")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
               item14, item15, item16, item17, item18, item19)
    return markup


def get_markup_leisure_types():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton("нет")
    item2 = types.KeyboardButton("бизнес-встречи")
    item3 = types.KeyboardButton("бранчи")
    item4 = types.KeyboardButton("вечеринки")
    item5 = types.KeyboardButton("dj-сеты")
    item6 = types.KeyboardButton("живая музыка")
    item7 = types.KeyboardButton("казино")
    item8 = types.KeyboardButton("караоке")
    item9 = types.KeyboardButton("компьютерный клуб")
    item10 = types.KeyboardButton("книжный магазин")
    item11 = types.KeyboardButton("конкурсы")
    item12 = types.KeyboardButton("конкурсы и сотрудничества")
    item13 = types.KeyboardButton("концерты")
    item14 = types.KeyboardButton("магазин пластинок")
    item15 = types.KeyboardButton("маркеты")
    item16 = types.KeyboardButton("настольные игры")
    item17 = types.KeyboardButton("спортивные трансляции")
    item18 = types.KeyboardButton("танцпол")
    item19 = types.KeyboardButton("тренинги")
    item20 = types.KeyboardButton("фестивали")
    item21 = types.KeyboardButton("Готово")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
               item14, item15, item16, item17, item18, item19, item20, item21)
    return markup


def get_markup_fit_types():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton("бизнес встречи")
    item2 = types.KeyboardButton("большой компании")
    item3 = types.KeyboardButton("быстрый перекус")
    item4 = types.KeyboardButton("взять с собой")
    item5 = types.KeyboardButton("встречи с друзьями")
    item6 = types.KeyboardButton("встречи с подругой")
    item7 = types.KeyboardButton("обед")
    item8 = types.KeyboardButton("отдых с друзьями")
    item9 = types.KeyboardButton("праздники")
    item10 = types.KeyboardButton("свидания")
    item11 = types.KeyboardButton("тусовки")
    item12 = types.KeyboardButton("учеба/работа")
    item13 = types.KeyboardButton("Готово")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
    return markup


def get_markup(atrName, atrTable):
    try:

        req = "SELECT DISTINCT {} FROM {} ORDER BY {}".format(atrName, atrTable, atrName)
        cursor.execute(req)
        my_result = cursor.fetchall()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        i = -1
        while i < len(my_result) - 3:

            i += 3
            markup.add(types.KeyboardButton(my_result[i-2][0]), types.KeyboardButton(my_result[i-1][0]),
                       types.KeyboardButton(my_result[i][0]))

        i = len(my_result) - i - 1

        if i == 1:

            markup.add(types.KeyboardButton(my_result[len(my_result)-1][0]), types.KeyboardButton("Готово"))

        elif i == 2:

            markup.add(types.KeyboardButton(my_result[-2][0]),
                       types.KeyboardButton(my_result[-1][0]), types.KeyboardButton("Готово"))

        elif i == 0:

            markup.add(types.KeyboardButton("Готово"))

        return markup

    except Exception as e:
        print("ERROR: get_markup")

