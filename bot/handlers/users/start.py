import logging

from asgiref.sync import sync_to_async

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot.models import TelegramUser
from bot.apps import get_login_url
from bot.const_text import c_get_hello_unregister, c_get_hello_register, c_register
from bot.keyboards.keyboards import button_with_link, make_buttons

from bot.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram_user, _ = await TelegramUser.objects.aget_or_create(chat_id=message.from_user.id)
    user = await sync_to_async(telegram_user.get_user)()
    if user is not None:
        logging.info("User already exists")
        await message.answer(
            text=c_get_hello_register(
                user.first_name,
                user.last_name),
            reply_markup=button_with_link({'Back to TEB': get_login_url()}))
    else:
        logging.info("New user")
        await message.answer(
            text=c_get_hello_unregister(message.from_user.full_name),
            reply_markup=make_buttons([c_register]))



