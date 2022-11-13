from aiogram.dispatcher.filters.state import *


class StatesGrp (StatesGroup):
    city = State()



class StatesSprav (StatesGroup):
    vibor_zap_poi = State()
    poisk = State()
    zapis_name = State()
    zapis_last_name = State()
    zapis_phone = State()