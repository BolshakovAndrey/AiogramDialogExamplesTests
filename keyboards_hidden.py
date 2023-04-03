from typing import Dict

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.text import Multi
from aiogram_dialog.widgets.when import Whenable


storage = MemoryStorage()
token = "5832323088:AAE-DaTZKGhWxQmc7EC4LYxPfEgIokUWOWs"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


# state.py
class MySG(StatesGroup):
    main = State()

# getter.py
async def get_data(**kwargs):
    return {
        "name": "Tishka17",
        "extended": True, # for example False or True
    }


# selected.py
def is_tishka17(data: Dict, widget: Whenable, manager: DialogManager):
    return data.get("name") == "Tishka17"


# keyboards.py


# __init__.py
dialog = Dialog(
    Window(
        Multi(
            Const("Hello"),
            Format("{name}", when="extended"),
            sep=" "
        ),
        Group(
            Row(
                Button(Const("Wait"), id="wait"),
                Button(Const("Ignore"), id="ignore"),
                when="extended",
            ),
            Button(Const("Admin mode"), id="nothing", when=is_tishka17),
        ),
        state=MySG.main,
        getter=get_data,
    )
)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
