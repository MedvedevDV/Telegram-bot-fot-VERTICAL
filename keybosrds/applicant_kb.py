from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # ReplyKeyboardRemove -

# полсе использования кнопки позволяет удалть кнопки
# reply_markup=ReplyKeyboardRemove() на нужной кнопке

b1 = KeyboardButton('Расположение')
b2 = KeyboardButton('Рабочее время')
b3 = KeyboardButton('Начать тестирование')
#b3 = KeyboardButton('/Meny')

# b4 = KeyboardButton('Поделиться номером', request_contact=True)  # кнопки исключения
# b5 = KeyboardButton('Поделиться местоположением', request_location=True)  #

kb_applicant = ReplyKeyboardMarkup(resize_keyboard=True)
                                   #one_time_keyboard=True)  # resize_keyboard=TRUE - меняет размер кнопки под содержимое
# one_time_keyboard=trye - позволяет после сипользования кнопки свернуть ее
# kb_applicant.add(b1).add(b2).insert(b3) # insetr - если есть место добавляет кнопку не с новой строки и рядом в строку

kb_applicant.row(b1, b2).add(b3)  # row - добавляет все (входные) кнопки в одну строку
# можно писать add.row.insert и смотреть как лучше выглюдит
