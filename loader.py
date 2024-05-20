import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

CHANNELS = [{
    'channel_id': "-1002008838927",
    'channel_name': "Python developer",
},{
    'channel_id': ":-1002117745999",
    'channel_name': "geeks_uz_group"
}]
ADMIN = os.getenv('ADMIN')
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=storage)


