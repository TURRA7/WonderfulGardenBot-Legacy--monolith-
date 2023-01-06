from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite1_db


# Start function.
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               'Здравствуйте! Вас приветствует магазин цветов - Чудесный сад!',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/***')


# The function of showing contacts.
async def command_contacts(message: types.Message):
    await message.reply("Н-о-м-е-р - и-м-я", reply_markup=ReplyKeyboardRemove())


# Function of the 'INDOOR FLOWERS' section.
async def Indoor_flowers_1(message: types.Message):
    await sqlite1_db.flor_menu_command_1(message)


# Function of the 'Garden Flowers' section.
async def Indoor_flowers_2(message: types.Message):
    await sqlite1_db.flor_menu_command_2(message)


# Function of the 'BOUQUETS' section.
async def Indoor_flowers_3(message: types.Message):
    await sqlite1_db.flor_menu_command_3(message)


# Registration of handlers.
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(
        command_contacts, lambda message: message.text == "📱КОНТАКТЫ📱")
    dp.register_message_handler(
        Indoor_flowers_1, lambda message: message.text == "🌺КОМНАТНЫЕ ЦВЕТЫ🌺")
    dp.register_message_handler(
        Indoor_flowers_2, lambda message: message.text == "🌹САДОВЫЕ ЦВЕТЫ🌹")
    dp.register_message_handler(
        Indoor_flowers_3, lambda message: message.text == "💐БУКЕТЫ💐")