from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def answer_btn(name, username, userid):
    if username:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=name, 
                        url=f"https://t.me/{username}"
                    )
                ],
                [
                    InlineKeyboardButton(text="Напишите ответ ✍️", callback_data=f'answer_{userid}')
                ]
            ]
        )
    else:
                return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                   InlineKeyboardButton(text=name, callback_data=f"user_private")
                ],
                [
                    InlineKeyboardButton(text="Напишите ответ ✍️", callback_data=f'answer_{userid}')
                ]
            ]
        )