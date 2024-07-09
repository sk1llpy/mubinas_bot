from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def cancel_btn():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="⬅️ Bekor qilish")
            ]
        ]
    )