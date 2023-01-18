from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_1 = KeyboardButton("/backend")
button_2 = KeyboardButton("/frontend")
button_3 = KeyboardButton("/uxui")
button_4 = KeyboardButton("/android")
button_5 = KeyboardButton("/ios")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)