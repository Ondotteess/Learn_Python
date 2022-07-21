import sqlite3 as sq
from create_bot import bot


def sql_start():
	global base, cur
	base = sq.connect('py_cool.db')
	cur = base.cursor()
	if base:
		print('Data base is connected')
	base.execute('CREATE TABLE IF NOT EXISTS menu(name TEXT PRIMARY KEY, description TEXT)')
	base.commit()

async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO menu VALUES(?, ?)', tuple(data.values()))
		base.commit()

async def sql_read(message):
	for ret in cur.execute('SELECT * FROM menu').fetchall():
		await bot.send_message(message.from_user.id, ret[0], ret[1])

