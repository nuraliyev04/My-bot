from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import ADMIN
class CheckAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if message.from_user.id == int(ADMIN):
            return True
        else:
            return False
