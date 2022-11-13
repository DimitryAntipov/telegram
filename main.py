from aiogram import types, executor
from keyboard import get_kb
from aiogram.utils import executor

from states import *
from create_bot import *
from pogoda import *
from ducks import *
from spravochnik import *



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Выбери то что тебе нужно на клавиатуре', reply_markup=get_kb())




dp.register_message_handler(cmd_weser, commands=['Погода']) 
dp.register_message_handler(cmd_ducks, commands=['Уточка']) 
dp.register_message_handler(cmd_spravochnik, commands=['Справочник'])







async def on_start(_):
    print("Бот запущен")
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
    