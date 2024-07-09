from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📨 Xabar yuborish")
            ]
        ]
    )