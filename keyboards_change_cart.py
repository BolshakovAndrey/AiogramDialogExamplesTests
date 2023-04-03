import operator

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.kbd import Button, Url, Column, Row, Group, ScrollingGroup, ManagedCheckboxAdapter, \
    Checkbox, Radio, Multiselect
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.text import Multi

storage = MemoryStorage()
token = "5832323088:AAH6wC9N4xmU8dm7z2nAGQj-phiTGnatmc4"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


# state.py
class MySG(StatesGroup):
    main = State()


# selected.py
async def check_changed(event: ChatEvent, checkbox: ManagedCheckboxAdapter, manager: DialogManager):
    print("Check status changed:", checkbox.is_checked())


# getters.py
async def get_data(**kwargs):
    fruits = [
        ("Витамин А (1) цена - 1000 ₽", '1'),
        ("Витамин D (1) цена - 1200 ₽", '2'),
        ("Витамин E (1) цена - 1500 ₽", '3'),
    ]
    return {
        "fruits": fruits,
        "count": len(fruits),
    }


# keyboards.py
fruits_kbd = Column(
    Radio(
        Format("☑️{item[0]}"),  # E.g `🔘 Apple`
        Format("🔲️ {item[0]}"),
        id="r_fruits",
        item_id_getter=operator.itemgetter(0),
        items="fruits",
    )
)

row = Row(
    Button(Const(" ➕ 1️⃣ "), id="go", ),
    Button(Const("Убрать 🗑️"), id="run", ),
    Button(Const(" ➖ 1️⃣ "), id="fly"),

)

# __init__.py
dialog = Dialog(
    Window('''Изменение корзины 🛒 !
 
Для выбора товара нажмите ☑️.
 
Для измените количества товара нажимайте ➕ 1️⃣  или  ➖ 1️⃣
 
Для удаления товара нажмите 🗑️.
 
Затем сохраните изменения 🆗.
 
Общая сумма: 3700 ₽
''',
           fruits_kbd,
           row,
           Button(Const("Сохранить изменения 🆗"), id="tele", ),
           Button(Const("Назад 🔚"), id="tele", ),
           Button(Const("В Каталог 💊"), id="tele",),
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
