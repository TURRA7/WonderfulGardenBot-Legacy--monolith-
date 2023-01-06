import sqlite3 as sq
from create_bot import bot


# Function for creating or connecting a database.
def sql_start():
    global base, cur
    base = sq.connect('chudesny_sad.db')
    cur = base.cursor()
    if base:
        print('Data base_1 connected OK!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS menu(img TEXT, \
            name TEXT PRIMARY KEY, description TEXT, price TEXT, save TEXT)')
    base.commit()


# The function of adding info to the database.
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?)',
                    tuple(data.values()))
        base.commit()


# The function of issuing lots (goods) No. 1 with a filter by section.
async def flor_menu_command_1(message):
    for ret in cur.execute('SELECT * FROM menu WHERE save = 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\
            Описание: {ret[2]}\nЦена {ret[3]}\nРаздел: {ret[4]}')


# The function of issuing lots (goods) No. 2 with a filter by section.
async def flor_menu_command_2(message):
    for ret in cur.execute('SELECT * FROM menu WHERE save = 2').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\
            Описание: {ret[2]}\nЦена {ret[3]}\nРаздел: {ret[4]}')


# The function of issuing lots (goods) No. 3 with a filter by section.
async def flor_menu_command_3(message):
    for ret in cur.execute('SELECT * FROM menu WHERE save = 3').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\
            Описание: {ret[2]}\nЦена {ret[3]}\nРаздел: {ret[4]}')


# The function of determining the lot (product) from the database
async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()


# The function of deleting a lot (product) from the database.
async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()
