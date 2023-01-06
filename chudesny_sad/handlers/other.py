import os
import json
import string
from aiogram import types, Dispatcher
from create_bot import dp, bot


# The mate filter function.
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


# Registration of filters.
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)