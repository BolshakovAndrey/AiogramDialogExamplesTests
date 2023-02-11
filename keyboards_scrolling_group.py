from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group, ScrollingGroup
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Multi

storage = MemoryStorage()
token = "5832323088:AAGvo9O-ERgPI5L4Bv_2PVYj3BuRn9ypuXU"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


# state.py
class MySG(StatesGroup):
    main = State()


# selected.py
async def on_quintity_selected(c: CallbackQuery, button: Button, manager: DialogManager):
    quanity = button.widget_id
    await c.message.answer(quanity)


# getters.py
def test_buttons_creator():
    btn_quantity = range(1, 21)
    buttons = []
    for i in btn_quantity:
        i = str(i)
        buttons.append(Button(Const(i), id=i, on_click=on_quintity_selected))
    return buttons


# keyboards.py
scrolling_group = ScrollingGroup(
    *test_buttons_creator(),
    id="numbers",
    width=5,
    height=2,
)

# __init__.py
dialog = Dialog(
    Window('Группа',
           scrolling_group,
           state=MySG.main,
           )
)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
