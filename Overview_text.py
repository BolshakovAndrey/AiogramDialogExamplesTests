from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text.multi import Multi

storage = MemoryStorage()
token = "5832323088:AAGvo9O-ERgPI5L4Bv_2PVYj3BuRn9ypuXU"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


class MySG(StatesGroup):
    main = State()


# getter.py
async def get_data(**kwargs):
    return {
        "name": "Tishka18",
    }


dialog = Dialog(
    # Window(
    #     # This will produce text `Hello! And goodbye!`
    #     Multi(
    #         Const("Hello!"),
    #         Const("And goodbye!"),
    #         sep=" ",
    #     ),
    #     state=MySG.main,
    # ),
    # Window(
    #     # This will produce text `Hello! And goodbye!`
    #     Multi(
    #         Format("Hello, {name}"),
    #         Const("and goodbye {name}!"),
    #         sep=", ",
    #     ),
    #     state=MySG.main,
    #     getter=get_data,  # data getter
    # ),
    Window(
        Multi(
            # Multi(Const("01"), Const("02"), Const("2003"), sep="."),
            Multi(Const("04"), Const("05"), Const("06"), sep=":"),
            sep="T"
        ),
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
