from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_social_ibtn():
    ibtn = InlineKeyboardMarkup()
    ibtn.add(InlineKeyboardButton('youtuube', url='https://www.youtube.com/'))
    ibtn.add(InlineKeyboardButton('google', url='https://www.google.com/'))
    return ibtn

async def get_voice_ibtn():
    ibtn1 = InlineKeyboardMarkup()
    ibtn1.add(InlineKeyboardButton('👍', callback_data = 'Like'))
    ibtn1.add(InlineKeyboardButton('👎', callback_data = 'Dislike'))
    return ibtn1
