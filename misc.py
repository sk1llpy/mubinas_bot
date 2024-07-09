from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from data.config import BOT_TOKEN


storage = MemoryStorage()
dp = Dispatcher(
    storage = storage
)
bot = Bot(
    token = BOT_TOKEN,
    default = DefaultBotProperties(
        parse_mode = ParseMode.HTML
    )
)