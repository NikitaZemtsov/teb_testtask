from aiogram.dispatcher.filters.state import StatesGroup, State


class UserRegister(StatesGroup):
    username = State()
    phone_number = State()
    first_name = State()
    last_name = State()
    email = State()
    password = State()

