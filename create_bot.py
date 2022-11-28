from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
# memori storage - позволяет зранить данные в оперативной памяти. при перезапуске стирается
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storege = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storege)
