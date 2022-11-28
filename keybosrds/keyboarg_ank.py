from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Архитектор')
b2 = KeyboardButton('Инженер-проетировщик')

kb_anketa = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(b2)