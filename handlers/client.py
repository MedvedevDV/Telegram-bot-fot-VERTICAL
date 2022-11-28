import time
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybosrds import kb_applicant


# @dp.message_handler(commands=['start']) декораторы нужны если бот в обном фале
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello Applicant', reply_markup=kb_applicant)
        await message.delete()
        time.sleep(2)
        await bot.send_message(message.from_user.id, 'Тут могла быть ваша реклама))')
    except:
        await message.reply(
            'Общение с ботом через ЛС, напишите ему: \nhttps://web.telegram.org/k/#@zerocity_the_croods_bot)')


# Список команд
# @dp.message_handler(commands=['Список команд'])
async def get_lst_comands(message: types.Message):
    await bot.send_message(message.from_user.id, ['start', 'Расположение', 'Рабочий график'])


# @dp.message_handler(commands=['Location'])
async def get_location_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           '\nhttps://yandex.ru/maps/org/vertikal/125299302272/?ll=65.572246%2C57.156041&z=16.57')


# @dp.message_handler(commands=['Рабочий график'])
async def get_worktime_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПН-ПТ с 9:00 до 18:00, СБ-ВС выходной')


@dp.message_handler(commands=['id'])
async def get_id(message: types.Message):
    id = message.from_user.id
    await bot.send_message(message.from_user.id, id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(get_location_command, lambda message: 'Расположение' in message.text)
    dp.register_message_handler(get_worktime_command, lambda message: 'Рабочее время' in message.text)
    dp.register_message_handler(get_id, lambda message: 'id' in message.text)
    dp.register_message_handler(get_lst_comands, lambda message: 'Список команд' in message.text)

    # Дискрипторы модно писать через lambda и выводить булевское значение по нужным фсвойствам -> можно в кнопке не писать /
