import operator
import os
from datetime import date

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ContentType

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group, ScrollingGroup, ManagedCheckboxAdapter, \
    Checkbox, Radio, Multiselect, Calendar, SwitchTo, Back, Next
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.text import Multi

storage = MemoryStorage()
token = "5832323088:AAEmcpRNspoK19fFdkOeJqJGJaS3sajBVHY"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


# state.py
class DialogSG(StatesGroup):
    first = State()
    second = State()
    third = State()


# selected.py
async def to_second(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.dialog().switch_to(DialogSG.second)


async def go_back(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.dialog().back()


async def go_next(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.dialog().next()


# __init__.py
class DialogSG(StatesGroup):
    first = State()
    second = State()
    third = State()


dialog = Dialog(
    Window(
        Const("First"),
        SwitchTo(Const("To second"), id="sec", state=DialogSG.second),
        state=DialogSG.first,
    ),
    Window(
        Const("Second"),
        Row(
            Back(),
            Next(),
        ),
        state=DialogSG.second,
    ),
    Window(
        Const("Third"),
        Back(),
        state=DialogSG.third,
    )
)

registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(DialogSG.first, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
