from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from aiogram import types

async def on_startup(_):
	print('status: online')
	sqlite_db.sql_start()

from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)


@dp.message_handler()
async def empty(message : types.Message):
	await message.answer('Несуществующая команда')
	await message.delete()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)