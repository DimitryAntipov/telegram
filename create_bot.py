from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

dp = Dispatcher(Bot(''), storage=MemoryStorage())
