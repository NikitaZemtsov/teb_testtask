from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.const_text import c_share_phone_number, c_cancel


def button_with_link(names:dict):
    keyboard = InlineKeyboardMarkup()
    for name, url in names.items():
        button = InlineKeyboardButton(name, url=url)
        keyboard.add(button)
    return keyboard

def make_buttons(words: list, row_width: int = 1) -> ReplyKeyboardMarkup:
    buttons_group = ReplyKeyboardMarkup(
        row_width=row_width, resize_keyboard=True)
    for word in words:
        if word is not None:
            buttons_group.insert(KeyboardButton(text=word))
    return buttons_group

contact_request_button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text=c_share_phone_number,
                request_contact=True
            )
        ],
        [
            KeyboardButton(c_cancel)
        ]
    ]
)