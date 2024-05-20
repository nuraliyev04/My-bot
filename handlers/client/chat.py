from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import *
from keyboards.default import get_social_btn, get_start_btn, get_start_admin
import requests
# from filters import CheckadminFilter
# import item

from loader import bot, dp

like = 0
dislike = 0

#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     if message.from_user.id == int(ADMIN):
#         await message.answer("Assalom aleykum ADMIN!!!", reply_markup=await get_start_admin())
#     else:
#         user = user.get_user_by_id(message.from_user.id)
#         print(user)
#         if not user:
#             fio = f"{message.from_user.first_name} {message.from_user.last_name}"
#             user.create_user(fio, message.from_user.username, message.from_user.id)
#         await message.answer("Assalom aleykum botimizga xush kelibsiz!", reply_markup=await get_start_btn())
#         await message.delete()


@dp.message_handler(commands=['voice'])
async def voice(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://cdn.misterlauncher.org/storage/servers/7302/1002fd14a3ff62b_big.jpg',
                         caption='Sizga yoqdimi', reply_markup=await get_voice_ibtn())
    await message.delete()


# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
# async def contact(message: types.Message):
#     dbusers.update_user(message.contact.phone_number, message.from_user.id)
#     await message.answer("Qabul qilindi!!")
#     print(message)
#     await message.delete()


@dp.callback_query_handler()
async def callback_query(call: types.CallbackQuery):
    global like, dislike
    if call.data == 'like':
        like += 1
        await call.answer(f"like {like}")
    elif call.data == 'dislike':
        dislike += 1
        await call.answer(f"dislike {dislike}")


@dp.callback_query_handler()
async def callback_query(call: types.CallbackQuery):
    await call.answer(call.data)
    global like, dislike


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Nima yordam kerak?", reply_markup=await get_social_btn())
    await message.delete()


@dp.message_handler(commands=['sticker'])
async def sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEL-epmJ7WwXOHndfaCf2qzRy3Rfk0IjQACYRMAAhNUMUq9lyl0lvILAAE0BA')
    await message.delete()


@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    response = requests.get("http://api.weatherapi.com/v1/current.json?key=637a0367057542d9936143247240705&q=Tashkent")
    res = response.json()
    name = res['location']["name"]
    country = res['location']['country']
    tz_id = res['location']['tz_id']
    localtime = res['location']['localtime']
    temp_c = res['current']['temp_c']
    wind_mph = res['current']['wind_mph']
    text = await text_weather(name, country, tz_id, localtime, temp_c, wind_mph)
    await message.answer(text, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['currency'])
async def weather(message: types.Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    res = response.json()
    for item in res:
        valyuta = item['Ccy']
        if valyuta == 'USD' or valyuta == 'EUR' or valyuta == 'RUB':
            name = item['CcyNm_UZ']
            rate = item['Rate']
            date = item['Date']
            text = f"""
            <b>{name}</b>
<em>Sana</em> - <b>{date}</b>
<b>{valyuta} - {rate}</b>"""
    await message.answer(text, parse_mode='HTML')

    await message.delete()

@dp.message_handler(commands=['books'])
async def books(message: types.Message):
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=backend")
    res = response.json()
    items = res["items"]
    for item in items:
        name = item['volumeInfo']['title']
        authors = item['volumeInfo']['authors']
        i=1
        for author in authors:
         author1 = f"{author}{',' if i != len(authors) else ','}"
         i += 1
        await bot.send_photo(message.chat.id,
                         photo=item['volumeInfo']['imageLinks']['thumbnail'],
                         caption=f"""
                         <em>Kitob nomi: </em><b>{name}</b>
<em>Mualliflari: </em><b>{author1}</b>
                                """, parse_mode='HTML')
    await message.delete()




@dp.message_handler(commands=['photo'])
async def photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://get.wallhere.com/photo/Mr-Robot-Elliot-Mr-Robot-glitch-art-fan-art-digital-art-Photoshop-monochrome-1273963.jpg')
    await message.delete()


# @dp.message_handler(commands=['aboutme'])
# async def aboutme(message: types.Message):
#     if message.from_user.id != int(ADMIN):
#         user = message.from_user
#
#         text = f"""<em>user -</em> <b>{user.id}</b>
# <em>fio -</em> <b>{user.full_name}</b>
# <em>username -</em> <b>{user.username}</b>
# <em>chat_id -</em> <b>{message.chat.id}</b>"""
#
#     await message.answer(text, parse_mode="HTML")


@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer('Hello')
    # await message.reply('Hello')
    print(message)
    await bot.send_message(chat_id=message.chat.id, text=message.text, reply_markup=ReplyKeyboardRemove())


async def text_weather(name, country, tz_id, localtime, temp_c, wind_mph):
    text = f"""
    <em>Shahar</em> - <b>{name}</b>
<em>Davlat</em> - <b>{country}</b>
<em>Vaqt mintaqasi</em> - <b>{tz_id}</b>
<em>Mahalliy vaqt</em> - <b>{localtime}</b>
<em>Xarorat</em> - <b>{'+' if temp_c > 0 else '-'}{temp_c}°C</b>
<em>Shamol</em> - <b>{wind_mph}</b>
        """
    return text
