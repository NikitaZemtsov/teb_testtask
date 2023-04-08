import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from asgiref.sync import sync_to_async

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from bot.loader import dp, bot
from bot.const_text import *
from bot.apps import get_login_url
from bot.models import TelegramUser
from bot.states import UserRegister
from bot.keyboards.keyboards import make_buttons, contact_request_button, button_with_link


@dp.message_handler(text=c_register)
async def register(message: types.Message):
    await UserRegister.username.set()
    await message.answer(
        text=c_input_username,
        reply_markup=make_buttons(
            words=[message.from_user.username, c_cancel]))


@dp.message_handler(state=UserRegister.username)
async def register(message: types.Message, state: FSMContext):
    await UserRegister.next()
    await message.answer(
        text=c_input_phone_number,
        reply_markup=contact_request_button)

    await state.update_data(username=message.text)


@dp.message_handler(state=UserRegister.phone_number, content_types='contact')
async def register(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    if not phone_number.startswith("+"):
        phone_number = "+" + phone_number

    await UserRegister.next()
    await message.answer(
        text=c_input_first_name,
        reply_markup=make_buttons(
            words=[message.from_user.first_name, c_cancel]))
    await state.update_data(phone_number=phone_number)


@dp.message_handler(state=UserRegister.first_name)
async def register(message: types.Message, state: FSMContext):
    await UserRegister.next()
    await message.answer(
        text=c_input_last_name,
        reply_markup=make_buttons(
            words=[message.from_user.last_name, c_cancel]))
    await state.update_data(first_name=message.text)


@dp.message_handler(state=UserRegister.last_name)
async def register(message: types.Message, state: FSMContext):
    await UserRegister.next()
    await message.answer(
        text=c_input_email,
        reply_markup=make_buttons(
            words=[c_cancel]))
    await state.update_data(last_name=message.text)


@dp.message_handler(state=UserRegister.email)
async def register(message: types.Message, state: FSMContext):
    await UserRegister.next()
    await message.answer(
        text=c_input_password,
        reply_markup=make_buttons(
            words=[c_cancel]))
    await state.update_data(email=message.text)


@dp.message_handler(state=UserRegister.password)
async def register(message: types.Message, state: FSMContext):
    password = message.text
    if len(password) < 4:
        await message.answer(
            text=c_input_password_again)
        await message.delete()
        return
    profile_photos = await message.from_user.get_profile_photos()
    if profile_photos.total_count > 0:
        photo_path = await bot.get_file(profile_photos.photos[0][1].file_id)
        photo_url = bot.get_file_url(photo_path.file_path)
    else:
        photo_url = ""
    user_info = await state.get_data()
    try:
        user = await get_user_model().objects.acreate(
            username=user_info.get('username'),
            first_name=user_info.get('first_name'),
            last_name=user_info.get('last_name'),
            email=user_info.get('email'),
            password=make_password(password))
        telegram_user = await TelegramUser.objects.aget(chat_id=message.from_user.id)
        await sync_to_async(telegram_user.set_data)(photo_url=photo_url, phone_number=user_info['phone_number'])
        await sync_to_async(telegram_user.set_user)(user)
        await message.answer(
            text=c_successfully_register,
            reply_markup=button_with_link({'Back to TEB': get_login_url()}))
        logging.info(f"{user.username} user was successfully created")
    except Exception as ex:
        await message.answer(
            text=str(ex),
            reply_markup=make_buttons([c_register]))

    await message.delete()
    await state.finish()


@dp.message_handler(Command(commands=["cancel"]), state=UserRegister)
async def stop_state(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(
        text=c_start,
        reply_markup=make_buttons(
            words=[c_register]))
