import sqlite3 as sql
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keybosrds import keyboarg_ank
from aiogram.types import ReplyKeyboardRemove


base = sql.connect('vert_questions_base')
cur = base.cursor()

data_AR = {}
data_IG = {}


class UserAR(StatesGroup):
    name = State()
    post = State()

    @staticmethod
    def init_UserAR_arg(count):
        for i in range(count):
            setattr(UserAR, f"question_{i}", State())


class UserIG(StatesGroup):
    name = State()
    post = State()

    @staticmethod
    def init_UserIG_arg(count):
        for i in range(count):
            setattr(UserAR, f"question_{i}", State())


# @dp.message_handler(commands=['Начать тестирование'], state=None)
async def command_start_test(message: types.Message):
    global data_AR, data_IG
    data_AR = cur.execute('SELECT * FROM ARquestions').fetchall()
    data_IG = cur.execute('SELECT * FROM INquestions').fetchall()
    await UserAR.name.set()
    await message.answer('Здравствуйте! \nВвседите ФИО')


# @dp.message_handler(state="*", commands="Закончить тестировани")
# @dp.message_handler(Text(equals='Закончить тестировани', ignore_case=True), state="*")
#def cancel_handler(message: types.Message, state: FSMContext):
 #   current_state = await state.get_state()
 #   if current_state is None:
 #       return
 #   await state.finish()
  #  await message.reply('Тест отменен')


# @dp.message_handler(state=Form.name)
async def procces_post(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Имя'] = message.text
    await Form.next()
    await message.answer('Ваша потенциальная должность?', reply_markup=keyboarg_ank.kb_anketa)


# @dp.message_handler(Text(equals='Архитектор', ignore_case=True), state=Form.post):
async def procces_ar(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Должность'] = message.text
    await Form.a_q1.set()
    await message.answer_photo(data_AR[0][1], f'Вопрос {data_AR[0][0]}\n{data_AR[0][2]}', reply_markup=ReplyKeyboardRemove())

    #await message.answer(data_AR[0][1], f'Вопрос {data_AR[0][0]}\n{data_AR[0][2]}')


# @dp.message_handler(state=Form.a_q1)
async def process_ARq1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['АР_В1'] = message.text
    await Form.next()
    await message.answer_photo(data_AR[1][1], f'Вопрос {data_AR[1][0]}\n{data_AR[1][2]}')

#  @dp.message_handler(state=Form.a_q2)
async def procces_ARq2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['АР_В2'] = message.text

    async with state.proxy() as data:
        await bot.send_message(776224718, str(data))

    await message.answer('Тестирование завершено. Тут можно записать отращение')
    await state.finish()


# @dp.message_handler(Text(equals='Инженер', ignore_case=True), state="*"):
async def procces_ig(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Должность'] = message.text
    await Form.i_q1.set()
    await message.answer_photo(data_IG[0][1], f'Вопрос {data_IG[0][0]}\n{data_IG[0][2]}', reply_markup=ReplyKeyboardRemove())


# dp.message_handler(state=Form.i_q1)
async def procces_IGq1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ИН_В1'] = message.text
    await Form.next()
    await message.answer_photo(data_IG[1][1], f'Вопрос {data_IG[1][0]}\n{data_IG[1][2]}')


# @dp.message_handler(state=Form.i_q2)
async def procces_IGq2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ИН_В2'] = message.text

    async with state.proxy() as data:
        await bot.send_message(776224718, str(data))

    await message.answer('Тестирование завершено. Тут можно записать отращение')
    await state.finish()


def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(command_start_test, lambda message: 'Начать' in message.text)
    # dp.register_message_handler(cancel_handler, state="*", commands="Закончить тестировани")
    # dp.register_message_handler(cancel_handler, Text(equals='Закончить тестировани', ignore_case=True), state="*")
    dp.register_message_handler(procces_post, state=Form.name)
    dp.register_message_handler(procces_ar, Text(equals='Архитектор', ignore_case=True), state=Form.post)
    dp.register_message_handler(process_ARq1, state=Form.a_q1)
    dp.register_message_handler(procces_ARq2, state=Form.a_q2)
    dp.register_message_handler(procces_ig, Text(equals='Инженер-проетировщик', ignore_case=True), state=Form.post)
    dp.register_message_handler(procces_IGq1, state=Form.i_q1)
    dp.register_message_handler(procces_IGq2, state=Form.i_q2)

