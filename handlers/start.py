from misc import dp, bot
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, StateFilter

from keyboards.default import menu, cancel
from keyboards.inline import answer

from states.send_letter import SendLetterState, SendAnswerState
from data.config import ADMIN
from db.database import get_user, add_user

@dp.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    user = get_user(message.from_user.id)

    if not user:
        add_user(message.from_user.id)

    if not message.from_user.id == ADMIN:
        if not await state.get_state():
            await message.answer(f"<b>Привет {message.from_user.full_name} 👋</b>", reply_markup=menu.menu())
        else:
            await message.answer("<b>Сообщение было отменено ❌</b>")
    else:
        if not await state.get_state():
            await message.answer(f"<b>Привет Мубина, добро пожаловать в бот 👋</b>", reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer("<b>Отменено ❌</b>")

@dp.message(lambda msg: msg.text == "📨 Задать вопрос")
async def send_letter_handler(message: types.Message, state: FSMContext):
    if not message.from_user.id == ADMIN:
        await state.set_state(SendLetterState.text)
        await message.answer("<b>Введите вопрос 👇</b>", reply_markup=cancel.cancel_btn())


@dp.message(lambda msg: msg.text == "⬅️ Отмена", StateFilter(SendLetterState.text))
async def send_letter_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("<b>Отменено ❌</b>", reply_markup=menu.menu())

@dp.message(lambda msg: msg.content_type == 'text', StateFilter(SendLetterState.text))
async def send_text_handler(message: types.Message, state: FSMContext):
    await message.answer("<b>Вопрос отправлено ✅</b>", reply_markup=menu.menu())

    try:
        await bot.send_message(chat_id=ADMIN, text=f"""<b>📨 Новое вопрос отправлено</b>

<i>{message.text}</i>""", reply_markup=answer.answer_btn(message.from_user.full_name,
                                                         message.from_user.username,
                                                         message.from_user.id))
    except: pass

    await state.clear()

@dp.callback_query(lambda call: call.data == 'user_private')
async def user_is_private_handler(call: types.CallbackQuery):
    await call.answer("Пользователь не идентифицирован ❌")

@dp.callback_query(lambda call: str(call.data).startswith("answer_"))
async def answer_to_letter_handler(call: types.CallbackQuery, 
                                   state: FSMContext):
    if call.from_user.id == ADMIN:
        await state.set_state(SendAnswerState.text)
        await state.set_data({'user_id': call.data.split("_")[1]})
        await call.message.answer("<b>Введите ответ 👇</b>", reply_markup=cancel.cancel_btn())

@dp.message(lambda msg: msg.text == "⬅️ Отмена", StateFilter(SendAnswerState.text))
async def answer_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("<b>Отменено ❌</b>", 
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message(lambda msg: msg.content_type == 'text', StateFilter(SendAnswerState.text))
async def send_text_handler(message: types.Message, state: FSMContext):

    data = await state.get_data()
    user_id = data['user_id']

    try:
        await bot.send_message(chat_id=int(user_id), text=f"""<b>📨 Ответ отправлен</b>

<i>{message.text}</i>""")
        await message.answer("<b>Ответ отправлен ✅</b>", reply_markup=types.ReplyKeyboardRemove())
    except:
        await message.answer("<b>Пользователь заблокировал бота ❌</b>", 
                             reply_markup=types.ReplyKeyboardRemove())

    await state.clear()