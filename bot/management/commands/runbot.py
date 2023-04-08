from django.core.management.base import BaseCommand
from aiogram import executor
from bot.handlers import *
from bot.loader import dp


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        executor.start_polling(dp, skip_updates=True)

