from states import StatesGrp
from aiogram.dispatcher import FSMContext
import requests
from aiogram import types
from create_bot import *


async def cmd_weser(message: types.Message):
    await message.answer ('Введи название города на латинице')
    await StatesGrp.city.set()
     

@dp.message_handler(state=StatesGrp.city)
async def load_city(message: types.Message, state: FSMContext):
    print ('прошел')
    async with state.proxy() as city_txt:
        city_txt = message.text
        print(city_txt)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_txt}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru"
        response = requests.get(url)
        a = response.json()
        temp = a['main']['temp']
        weather = a['weather'][0]['description']

    await message.answer(f"В городе - {city_txt}, температура воздуха - {temp}; Обращаем Ваше внимание, что - {weather} ")
    await state.finish()


