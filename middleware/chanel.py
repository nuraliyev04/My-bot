from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from loader import *
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CustomMiddleware(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):
        print(message.text)
        if not message.text != "/start":
            user = message.from_user
            if user.username:
                for channel in CHANNELS:
                    user_channels = await bot.get_chat_member(user_id=int(user.id), chat_id=channel.get('channel_id'))
                    if user_channels.status == "left":
                        ibtn = InlineKeyboardMarkup()
                        ibtn.add(
                            InlineKeyboardButton(text="A'zo bolish", url=f"https://t.me/{channel.get('channel_id')}"))
                        await message.answer(f"Siz bu@{channel.get('channel_name')}kanalga a'zo bo'lmagansiz",
                                             reply_markup=ibtn)
                        raise CancelHandler()
            else:
                await message.answer("Username is required")
                raise CancelHandler()
        else:
            ibtn = InlineKeyboardMarkup()
            for channel in CHANNELS:
                ibtn.add(InlineKeyboardButton(text="A'zo bolish", url=f"https://t.me/{channel.get('channel_id')}"))

            await message.answer('Botimizga xush kelibsiz:', reply_markup=ibtn)

