import operator
from typing import Any

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group, ScrollingGroup, ManagedCheckboxAdapter, \
    Checkbox, Select
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.text import Multi

storage = MemoryStorage()
token = "5832323088:AAGvo9O-ERgPI5L4Bv_2PVYj3BuRn9ypuXU"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


# state.py
class MySG(StatesGroup):
    main = State()


# getters.py
async def get_data(**kwargs):
    quianity = [
        ("1 шт", '1'),
        ("2 шт", '2'),
        ("3 шт", '3'),
        ("4 шт", '4'),
    ]
    return {
        "items": quianity,
        "count": quianity,
    }


# selected.py
async def on_count_selected(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    print("Button selected: ", item_id)
    return item_id


# keyboards.py
fruits_kbd = Select(
    Format("{item[0]}"),
    id="s_counts",
    item_id_getter=operator.itemgetter(1),  # each item is a tuple with id on a first position
    items="items",  # we will use items from window data at a key `items`
    on_click=on_count_selected,
)

# window.py
dialog = Dialog(
    Window('Выберите количетсво',
           fruits_kbd,
           state=MySG.main,
           getter=get_data,  # data getter
           )
)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
