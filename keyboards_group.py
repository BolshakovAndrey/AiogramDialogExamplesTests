from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group
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
async def clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    await c.message.answer("Click!")


# keyboards.py
group = Group(
    Button(Const("Crawl"), id="crawl", on_click=clicked),
    Button(Const("Go"), id="go", on_click=clicked),
    Button(Const("Run"), id="run", on_click=clicked),
    Button(Const("Fly"), id="fly", on_click=clicked),
    Button(Const("Teleport"), id="tele", on_click=clicked),
    width=2,
)

row = Row(
    Button(Const("Go"), id="go", on_click=clicked),
    Button(Const("Run"), id="run", on_click=clicked),
    Button(Const("Fly"), id="fly"),
)

column = Column(
    Button(Const("Go"), id="go", on_click=clicked),
    Button(Const("Run"), id="run", on_click=clicked),
    Button(Const("Fly"), id="fly", on_click=clicked),
)

# __init__.py
dialog = Dialog(
    Window('Группа',
           group,
           row,
           column,
           state=MySG.main,
           )
)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
