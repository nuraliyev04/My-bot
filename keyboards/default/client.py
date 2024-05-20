from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def get_start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton('/start')).insert(KeyboardButton('/help'))
    btn.add(KeyboardButton('/sticker')).insert(KeyboardButton('/more information')).insert(KeyboardButton('/aboutme'))
    btn.add(KeyboardButton('/another_bot')).insert(KeyboardButton('/youtube')).insert(KeyboardButton('/voice')).insert(KeyboardButton('/contact', request_contact=True))
    return btn

async def get_social_btn():
    btn2 = ReplyKeyboardMarkup(resize_keyboard=True)
    btn2.add(KeyboardButton('/photo'))
    return btn2
