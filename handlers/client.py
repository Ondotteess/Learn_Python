from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_materials_client, url_lib_kb, url_self_learn_kb, url_playlists_kb, url_tasks_kb, urlkb
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Что умеет бот этот?\n\nБот хранит ссылки на ресурсы, незаменимые при изучении\
языка программирования Python. Все ресурсы поделены на 3 категории:\n\
• Учебные материалы\n\
• Форумы\n\
• Задачники\n', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение в лс бота')


@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)


async def study_materials_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Ниже представлен перечень учебных материалов, каталогизированныхпо форме подачи информации.\n\n \
Изучение предпочтительнее начинать с видеокурсов, перемежая просмотр чтением\
тематических статей. К учебной литературе рекомендуется переходить после просмотра курса.', reply_markup=kb_materials_client)


async def forums_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Список наиболее популярных русскоязычных форумов для программистов,\
 где можно найти решение проблемы или задать вопрос самому.', reply_markup=urlkb)

async def book_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Книги', reply_markup=url_lib_kb)

async def self_learn_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Самоучители', reply_markup=url_self_learn_kb)

async def tasks_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Список наиболее популярных задачников по программированию.', reply_markup=url_tasks_kb)

async def playlists_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Видеокурсы', reply_markup=url_playlists_kb)



@dp.message_handler(commands=['Функции'])
async def function_db_command(message : types.Message):
	await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help', 'назад'])
	dp.register_message_handler(pizza_menu_command, commands=['Меню'])
	dp.register_message_handler(study_materials_command, commands=['Учебные_материалы'])
	dp.register_message_handler(forums_command, commands=['Форумы'])
	dp.register_message_handler(tasks_command, commands=['Задачники'])
	dp.register_message_handler(book_command, commands=['Книги'])
	dp.register_message_handler(self_learn_command, commands=['Самоучители'])
	dp.register_message_handler(playlists_command, commands=['Видеокурсы'])
	dp.register_message_handler(function_db_command, commands=['Функции'])