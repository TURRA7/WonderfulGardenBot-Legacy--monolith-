from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# Start window buttons.
b1 = KeyboardButton('🌺КОМНАТНЫЕ ЦВЕТЫ🌺')
b2 = KeyboardButton('🌹САДОВЫЕ ЦВЕТЫ🌹')
b3 = KeyboardButton('💐БУКЕТЫ💐')
b4 = KeyboardButton('📱КОНТАКТЫ📱')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1, b2).add(b3, b4)