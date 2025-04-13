from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.markdown import hbold
from config import TOKEN
from handlers import register_handlers

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

register_handlers(dp)

async def on_startup(dispatcher):
    print("Bot ishga tushdi")

if name == "main":
    import asyncio
    async def main():
        print("Bot ishga tushmoqda...")
        await dp.start_polling(bot)

    asyncio.run(main())
