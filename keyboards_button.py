# from aiogram import Bot, Dispatcher, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.types import Message, CallbackQuery
#
# from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
# from aiogram_dialog.widgets.kbd import Button, Url
# from aiogram_dialog.widgets.text import Const
# from aiogram_dialog.widgets.text import Multi
#
# storage = MemoryStorage()
# token = "5832323088:AAGvo9O-ERgPI5L4Bv_2PVYj3BuRn9ypuXU"
# bot = Bot(token)
# dp = Dispatcher(bot, storage=storage)
# registry = DialogRegistry(dp)
#
#
# # state.py
# class MySG(StatesGroup):
#     main = State()
#
#
# # getter.py
# async def get_data(**kwargs):
#     return {"name": "Tishka18", }
#
#
# # selected.py
# async def go_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
#     await c.message.answer("Going on!")
#
#
# dialog = Dialog(
#     Window(
#         Multi(
#             Const("Hello!"),
#             Const("And goodbye!"),
#             sep=" ",
#         ),
#         Button(
#             Const("Go"),
#             id="go",  # id is used to detect which button is clicked
#             on_click=go_clicked,
#         ),
#         Url(
#             Const("Github"),
#             Const('https://github.com/Tishka17/aiogram_dialog/'),
#         ),
#         state=MySG.main,
#         getter=get_data,  # data getter
#     ))
#
# registry.register(dialog)
#
#
# @dp.message_handler(commands=["start"])
# async def start(m: Message, dialog_manager: DialogManager):
#     await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
