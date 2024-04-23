import types

from loads import bot, dp
from keyboards.default import get_start
from keyboards.inline import get_social
from keyboards import

@dp.message_handler(commands=['sticker'])
async def sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAEL891mIoe8D23EC4AZoIyjslV4qW72jwACkRIAAvzw4UodOfjG8l2MszQE')

    HELP_COMMANDS = f"""""
    <em>/start</em> - <b>botni ishga tushirish</b>
    <help> - bot haqida ma'lumot
    <photo> - rasim junatish
    """

@dp.callback_query_handler()
async def callback_handler(call: types.CallbackQuery):
    if call.data == 'google':
        await call.answer('google bosildi')
    elif call.data == 'youtube':
        await call.answer('youtube bosildi')

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    print(message)
    # await bot.send_message(chat_id=message.chat.id, text=message.text)
    await message.answer('Botimizga xush kelibsiz', reply_markup=btn)