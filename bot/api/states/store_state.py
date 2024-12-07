from aiogram.fsm.state import State, StatesGroup


class AddProductStoreState(StatesGroup):
    body = State()