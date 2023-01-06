import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Data storage in RAM.
storage = MemoryStorage()


# Initializing the dispatcher and bot.
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)