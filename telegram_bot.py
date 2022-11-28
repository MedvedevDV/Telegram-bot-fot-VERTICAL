from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

from handlers import client, other, admin  #импотр функций бота
from anketa import ank

async def one_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_add_ARquestions()
    sqlite_db.sql_add_INquestions()

# ''''******************************Пользоватльская часть******************************''''
client.register_handlers_client(dp)
ank.register_handlers_anketa(dp)
# ''''******************************Административная часть******************************''''
admin.register_handlers_admin(dp)
# ''''******************************Общая часть******************************''''
other.register_handlers_other(dp) #пустой hendler внизу
# модуль фильтра мата



#    await message.answer(message.text) # простоя запись в чат(личка или группа)
#    await message.reply(message.text) # ответ с упоминанием автора(личка или группа)
#    await bot.send_message(message.from_user.id, message.text) # ответ в личку (бот не может написать первым)



executor.start_polling(dp, skip_updates=True, on_startup=one_startup) # skip_updates бот не будеь отчечать на сообщения написаннгый когда он офлайн

if __name__ == '__main__':
    pass

