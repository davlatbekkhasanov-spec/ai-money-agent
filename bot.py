import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🔥 AI Agent ишга тушди!\n/idea ёз")

@dp.message(Command("idea"))
async def idea(message: types.Message):
    await message.answer(
        "💡 Бугунги пул топиш идеяси:\n\n"
        "Telegram канал оч:\n"
        "- Бизнес / мотивация нишаси\n"
        "- Кунига 3 пост\n"
        "- Кейин PDF ёки хизмат сот"
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer("Мен ишлаяпман 😎")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
