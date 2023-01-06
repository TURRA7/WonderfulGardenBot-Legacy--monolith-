from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# Admin keyboard Buttons.
button_load_1 = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')


button_case_admin = ReplyKeyboardMarkup(
    resize_keyboard=True).add(button_load_1).add(button_delete)