from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keybosrds import keybord_adm

ID = 776224718


class FSMadmin(StatesGroup):
    namber = State()
    photo = State()
    question = State()
    post = State()


# Получаем ID админа бота и через if вводим
# @dp.message_handler(commands=['admin'])
async def admin_appointment(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Админимтратор назначен. Что нужно?', reply_markup=keybord_adm.button_case_admin)
    await message.delete()


# начало диалога для загрузки вопроса
# @dp.message_handler(commands='записать вопрос', state=None)#state=None нужно писать так как бот находитьсч не в ржиме машины состояниясотсяния
async def cm_start(message: types.Message):
    if ID == 776224718:
        await FSMadmin.namber.set()
        await message.reply('Введите номер вопроса')


# ловим номер
# @dp.message_handler(state=FSMadmin.namber)
async def loag_namber(message: types.Message, state: FSMContext):
    if ID == 776224718:
        async with state.proxy() as data: # словарь data заполняется по Ходу зополнения и можно в конце записать в базу уже сформированный
            data['namber'] = message.text
        await FSMadmin.next()
        await message.reply('Теперь загрузите фото')


# команда отмены
# @dp.message_handler(state="*", commands="отмена"):
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*"):
async def cancel_handler(message: types.Message, state: FSMContext):
    if ID == 776224718:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Загрузка отменена')


#  ловим photo
# @dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if ID == 776224718:
        try:
            async with state.proxy() as data:
                data['photo'] = message.photo[0].file_id
            await FSMadmin.next()
            await message.reply('Теперь введите вопрс')
        except:
            await FSMadmin.next()


# ловит question полдений ответ
# @dp.message_handler(state=FSMadmin.question)
async def loag_question(message: types.Message, state: FSMContext):
    if ID == 776224718:
        async with state.proxy() as data:
            data['question'] = message.text
            await FSMadmin.next()
            await message.reply('Для какой должности вопросы?', reply_markup=keybord_adm.button_case_post)


@dp.message_handler(state=FSMadmin.post)
async def post(message: types.Message, state: FSMContext):
    if ID == 776224718 and message.text == 'Архитектор':
        await sqlite_db.sql_add_command_ARquestions(state)
        # async with state.proxy() as data:
            # await message.reply(str(data)) отправка даных в чат телеграмм
        await state.finish()  # после исполнения сотет все введенные данные а режиме машины состояний
    elif ID == 776224718 and message.text == 'Инженер':
        await sqlite_db.sql_add_command_INquestions(state)
        await state.finish()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, lambda message: 'Записать' in message.text, state=None)
    dp.register_message_handler(cancel_handler, state="*", commands="отмена")
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(loag_namber, state=FSMadmin.namber)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(loag_question, state=FSMadmin.question)
    dp.register_message_handler(admin_appointment, commands=['admin'])
    dp.register_message_handler(post, state=FSMadmin.post)
