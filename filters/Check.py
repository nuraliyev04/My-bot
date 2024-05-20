from aiogram import types
from loader import ADMIN
from aiogram.dispatcher.filters import BoundFilter

class Check(BoundFilter):
    async def check(self, message: types) -> bool:
        if message.from_user.id == int(ADMIN):
            return True
        else:
            return False
