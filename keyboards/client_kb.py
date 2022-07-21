from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


b1 = KeyboardButton('/help')
b2 = KeyboardButton('/Учебные_материалы')
b3 = KeyboardButton('/Форумы')
b4 = KeyboardButton('/Задачники')


b2_1 = KeyboardButton('/Книги')
b2_2 = KeyboardButton('/Видеокурсы')
b2_3 = KeyboardButton('/Самоучители')
b2_4 = KeyboardButton('/назад')



url_lib_kb = InlineKeyboardMarkup(row_width=1)
url_self_learn_kb = InlineKeyboardMarkup(row_width=1)
url_playlists_kb = InlineKeyboardMarkup(row_width=1)
url_tasks_kb = InlineKeyboardMarkup(row_width=1)
urlkb = InlineKeyboardMarkup(row_width=1)


'''**************************Блок с КНИГАМИ**************************'''
urlButton2_1 = InlineKeyboardButton(text='Charles Severance — Введение в программирование (2016)', url='https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FBd\
Nf8IPLG7xHTe5c3AhyQkYpcPGyAE4QkA9OF7NRT1U%3D%3A%2FCharles%20Severance%20%E2%80%94%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%BF%D1%80%D0%BE%D0%\
B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20(2016).pdf&name=Charles%20Severance%20%E2%80%94%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0\
%B8%D0%B5%20%D0%B2%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20(2016).pdf')

urlButton2_2 = InlineKeyboardButton(text='Jason R. Briggs — Python для детей (2017)', url='https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FBdNf8IPLG7xHTe5c\
3AhyQkYpcPGyAE4QkA9OF7NRT1U%3D%3A%2FJason%20R.%20Briggs%20%E2%80%94%20Python%20%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%B5%D1%82%D0%B5%D0%B9%20(2017).pdf&name=Jason%20R.%20B\
riggs%20%E2%80%94%20Python%20%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%B5%D1%82%D0%B5%D0%B9%20(2017).pdf&nosw=1')

urlButton2_3 = InlineKeyboardButton(text='Python на практике (2014)', url='https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FBdNf8IPLG7xHTe5c3AhyQkYpcPGyAE4Q\
kA9OF7NRT1U%3D%3A%2Fpython%20%D0%BD%D0%B0%20%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B5%20(2014)%20(%2B%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B).pdf&n\
ame=python%20%D0%BD%D0%B0%20%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B5%20(2014)%20(%2B%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B).pdf&nosw=1')

urlButton2_4 = InlineKeyboardButton(text='Скрапинг веб-сайтов с помощью Python', url='https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2F6wTxvodCm0Pff587G4ADlY\
wyPXO1ddlwCMtg7KsprGk%3D%3A%2FPython%2F%D0%A1%D0%BA%D1%80%D0%B0%D0%BF%D0%B8%D0%BD%D0%B3%20%D0%B2%D0%B5%D0%B1-%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%20%D1%81%20%D0%BF%D0%B\
E%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20Python.pdf&name=%D0%A1%D0%BA%D1%80%D0%B0%D0%BF%D0%B8%D0%BD%D0%B3%20%D0%B2%D0%B5%D0%B1-%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%20%D1%81%20\
%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20Python.pdf&nosw=1')

urlButton2_5 = InlineKeyboardButton(text='Рамальо Лучано. Python. К вершинам мастерства.', url='https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2F6wTxvodCm0Pff\
587G4ADlYwyPXO1ddlwCMtg7KsprGk%3D%3A%2FPython%2F%D0%A0%D0%B0%D0%BC%D0%B0%D0%BB%D1%8C%D0%BE%20%D0%9B%D1%83%D1%87%D0%B0%D0%BD%D0%BE.%20Python.%20%D0%9A%20%D0%B2%D0%B5%D1%8\
0%D1%88%D0%B8%D0%BD%D0%B0%D0%BC%20%D0%BC%D0%B0%D1%81%D1%82%D0%B5%D1%80%D1%81%D1%82%D0%B2%D0%B0.pdf&name=%D0%A0%D0%B0%D0%BC%D0%B0%D0%BB%D1%8C%D0%BE%20%D0%9B%D1%83%D1%87%D\
0%B0%D0%BD%D0%BE.%20Python.%20%D0%9A%20%D0%B2%D0%B5%D1%80%D1%88%D0%B8%D0%BD%D0%B0%D0%BC%20%D0%BC%D0%B0%D1%81%D1%82%D0%B5%D1%80%D1%81%D1%82%D0%B2%D0%B0.pdf&nosw=1')


'''**************************Блок с САМОУЧИТЕЛЯМИ**************************'''
urlButton3_1 = InlineKeyboardButton(text='PythonTutor', url='https://pythontutor.ru/')
urlButton3_2 = InlineKeyboardButton(text='Codebra', url='https://codebra.ru/ru/courses/python')
urlButton3_3 = InlineKeyboardButton(text='Pythonworld', url='https://pythonworld.ru/samouchitel-python')


'''**************************Блок с ВИДЕОКУРСАМИ**************************'''
urlButton4_1 = InlineKeyboardButton(text='itProger', url='youtube.com/playlist?list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa')
urlButton4_2 = InlineKeyboardButton(text='egoroff', url='https://www.youtube.com/playlist?list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6')
urlButton4_3 = InlineKeyboardButton(text='Тимофей Хирьянов', url='https://www.youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0')


'''**************************Блок с ЗАДАЧАМИ**************************'''
urlButton5_1 = InlineKeyboardButton(text='tProger', url='https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/')
urlButton5_2 = InlineKeyboardButton(text='Leetcode', url='https://leetcode.com/problemset/all/')
urlButton5_3 = InlineKeyboardButton(text='Smartiqa', url='https://smartiqa.ru/courses/python/answer-key')
urlButton5_4 = InlineKeyboardButton(text='Сайт Полякова (для подготовки к ЕГЭ)', url='https://kpolyakov.spb.ru/school/ege/generate.htm')


'''**************************Блок с ФОРУМАМИ**************************'''
urlButton1 = InlineKeyboardButton(text='Stack Overflow', url='https://ru.stackoverflow.com')
urlButton2 = InlineKeyboardButton(text='Habr Q&A', url='https://qna.habr.com/')
urlButton3 = InlineKeyboardButton(text='CyberForum', url='https://www.cyberforum.ru')
urlButton4 = InlineKeyboardButton(text='Двач', url='https://2ch.hk/pr/catalog.html')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_materials_client = ReplyKeyboardMarkup(resize_keyboard=True)


url_lib_kb.add(urlButton2_1).add(urlButton2_2).add(urlButton2_3).add(urlButton2_4).add(urlButton2_5)
url_self_learn_kb.add(urlButton3_1).add(urlButton3_2).add(urlButton3_3)
url_playlists_kb.add(urlButton4_1).add(urlButton4_2).add(urlButton4_3)
url_tasks_kb.add(urlButton5_1).add(urlButton5_2).add(urlButton5_3).add(urlButton5_4)
urlkb.add(urlButton1).add(urlButton2).add(urlButton3).add(urlButton4)


kb_client.add(b1).row(b2, b3, b4)
kb_materials_client.row((b2_1), (b2_2), (b2_3)).add(b2_4)