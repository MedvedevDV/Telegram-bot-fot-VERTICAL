from aiogram import types, Dispatcher
from create_bot import dp
import json, string


# @dp.message_handler() #событие в чате
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('мат.json')))) != set():
        await message.reply('Материться тут незачем!')
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)