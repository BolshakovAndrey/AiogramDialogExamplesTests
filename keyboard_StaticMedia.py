import operator
import os
from datetime import date

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ContentType

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group, ScrollingGroup, ManagedCheckboxAdapter, \
    Checkbox, Radio, Multiselect, Calendar
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.text import Multi

storage = MemoryStorage()
token = "5832323088:AAE-DaTZKGhWxQmc7EC4LYxPfEgIokUWOWs"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


# state.py
class MySG(StatesGroup):
    main = State()


# __init__.py
dialog = Dialog(
    Window(
        Const("Greetings!"),
        StaticMedia(
            path=os.path.join("img.png"),
            type=ContentType.PHOTO,
        ),
        state=MySG.main,
    )
)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
