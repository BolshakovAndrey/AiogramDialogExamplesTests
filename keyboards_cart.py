from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Multi

storage = MemoryStorage()
token = "5832323088:AAEmcpRNspoK19fFdkOeJqJGJaS3sajBVHY"
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
    Button(Const("Оформить заказ 🆗"), id="tele", on_click=clicked),
    Button(Const("Изменить товары в корзине 🔄"), id="tele", on_click=clicked),
    Button(Const("Очистить корзину 🗑"), id="tele", on_click=clicked),
    Button(Const("Назад 🔚"), id="tele", on_click=clicked),
    Button(Const("В Каталог 💊"), id="tele", on_click=clicked),

    width=1,
)

column = Column(
    Button(Const("Витамин С (1) цена - 1000 ₽"), id="peels", on_click=clicked),
    Button(Const("Витамин D (1) цена - 1200 ₽"), id="capsuls", on_click=clicked),
    Button(Const("Витамин E (1) цена - 1500 ₽"), id="gums", on_click=clicked),
)

# __init__.py
dialog = Dialog(
    Window('''
    Корзина товаров 🛒 !
    
На общую сумму: 3700 ₽
    '''

           ,
           column,
           # row,
           group,
           state=MySG.main,
           )
)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
