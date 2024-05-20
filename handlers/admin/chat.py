from aiogram.dispatcher import FSMContext
from loader import dp, bot, ADMIN
from aiogram import types
from utils.database import users as dbusers
from states import MyStates
from filters import CheckAdmin


@dp.message_handler(CheckAdmin(), commands=['users'])
async def users(message: types.Message):
    user = dbusers.get_users()
    for item in user:
        text = get_text(item[0], item[1], item[2], item[3], item[4])
        await message.answer(text, parse_mode="HTML")


# await bot.send_photo(chat_id=message.chat.id,
#                      photo='https://cdn.misterlauncher.org/storage/servers/7302/1002fd14a3ff62b_big.jpg',
#                      caption='Sizga yoqdimi', reply_markup=await get_voice_ibtn())
# await message.delete()


@dp.message_handler(commands=['post'])
async def users(message: types.Message):
    if message.from_user.id == int(ADMIN):
        await message.answer('Xabarni kiriting:')
        await MyStates.request_message.set()


@dp.message_handler(state=MyStates.request_message)
async def request_message(message: types.Message):
    user = dbusers.get_users()
    for item in user:
        await bot.send_message(chat_id=item[4], text=message.text)


def get_text(a, b, c, d, e):
    text = f"""<em>user -</em> <b>{a}</b>
<em>fio -</em> <b>{b}</b>
<em>username -</em> <b>{c}</b>
<em>phone -</em> <b>{d}</b>
<em>chat_id -</em> <b>{e}</b>"""
    return text


@dp.message_handler(commands=['post'])
async def users(message: types.Message):
    if message.from_user.id == int(ADMIN):
        await message.answer('Xabarni kiriting:')
        MyStates.request_message.set()

# text = f"""
# <em>user -<em>: {item[0]},
# <em>fio -<em>: {item[1]},
#   <em>username -<em>: {item[2]},
# <em>phone -<em>: {item[3]}
#         <em>chat_id -<em>: {4}
# """
