from aiogram import types, executor

import requests







async def cmd_ducks(message: types.Message):
    response = requests.get(f"https://random-d.uk/api/random")
    ducks = response.json()
    await message.answer (ducks['url'])
    