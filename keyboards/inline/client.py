from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_social():
    ibtn = InlineKeyboardMarkup()
    ibtn = ibtn.add(InlineKeyboardButton('Google', callback_data="google"))
    ibtn = ibtn.add(InlineKeyboardButton('Youtube', callback_data="youtube"))
    return ibtn