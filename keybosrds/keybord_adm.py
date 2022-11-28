from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('Записать вопрос')
button_load_ar = KeyboardButton('Архитектор')
button_load_in = KeyboardButton('Инженер')
button_delete = KeyboardButton('Удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)
button_case_post = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load_ar).add(button_load_in)