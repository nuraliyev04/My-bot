from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_start_admin():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton('/start')).insert(KeyboardButton('help'))
    btn.add(KeyboardButton('/users')).insert(KeyboardButton('/post'))
    return btn