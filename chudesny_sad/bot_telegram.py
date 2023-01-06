import os
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite1_db
from handlers import client, admin, other


# bot function online.
async def on_startup(_):
    print('Бот вышел в онлайн!')
    sqlite1_db.sql_start()


# Connecting handlers.
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)