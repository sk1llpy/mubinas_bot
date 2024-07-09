from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from aiogram import Bot

async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand(command='start', description='Botni ishga tushurish 🤖'),
            BotCommand(command='help', description='Yordam ℹ️')
        ],
        scope=BotCommandScopeAllPrivateChats()
    )