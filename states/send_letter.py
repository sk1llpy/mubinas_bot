from aiogram.fsm.state import State, StatesGroup

class SendLetterState(StatesGroup):
    text = State()

class SendAnswerState(StatesGroup):
    text = State()