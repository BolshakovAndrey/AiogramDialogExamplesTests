from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Group
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text.multi import Multi

storage = MemoryStorage()
token = "5832323088:AAH6wC9N4xmU8dm7z2nAGQj-phiTGnatmc4"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


class MySG(StatesGroup):
    main = State()


# keyboards.py
group = Group(
    Button(Const("Каталог 💊"), id="tele"),
    Button(Const("Изменить товары в корзине 🔄"), id="tele"),
    Button(Const("Очистить корзину 🗑"), id="tele"),
    Button(Const("Выйти 🔚"), id="tele"),

    width=1,
)


# getter.py
async def get_data(**kwargs):
    return {
        "name": "Tishka18",
    }


dialog = Dialog(
    Window(
        Const(
            f'Ваш заказ №1456 от "04:05:06 успешно принят. Ожидайте подтверждения и реквизитов для оплаты.',
        ),
        group,
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
