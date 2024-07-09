import asyncio

from misc import dp, bot

from utils import logging
from utils.set_commands import set_default_commands
from db.database import create_table

import handlers


async def polling():
    create_table()

    await set_default_commands(bot)
    await dp.start_polling(bot)


def main():
    asyncio.run(polling())