from django.conf import settings
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

