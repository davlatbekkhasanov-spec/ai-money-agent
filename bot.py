import asyncio
import logging
import os
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================= START =================
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔥 AI MONEY AGENT\n\n"
        "Командалар:\n"
        "/idea - пул топиш ғояси\n"
        "/niche - ниша танлаш\n"
        "/plan - кунлик план\n"
        "/sell - нима сотиш мумкин\n"
    )

# ================= IDEA =================
@dp.message(Command("idea"))
async def idea(message: types.Message):
    ideas = [
        "Telegram канал очиб, PDF ва чек-лист сотиш",
        "Instagram орқали товар сотиш (дропшиппинг)",
        "Фриланс хизмат (бот, сайт, дизайн)",
        "Affiliate маркетинг (бошқалар маҳсулотини сотиш)",
        "Контент канал + реклама орқали даромад"
    ]
    await message.answer(f"💡 Ғоя:\n{random.choice(ideas)}")

# ================= NICHE =================
@dp.message(Command("niche"))
async def niche(message: types.Message):
    niches = [
        "Бизнес ва пул топиш",
        "Саломатлик ва фитнес",
        "Технология ва AI",
        "Онлайн савдо",
        "Шахсий ривожланиш"
    ]
    await message.answer(f"📊 Тавсия ниша:\n{random.choice(niches)}")

# ================= PLAN =================
@dp.message(Command("plan"))
async def plan(message: types.Message):
    await message.answer(
        "📅 Бугунги план:\n\n"
        "1. 1 та ниша танла\n"
        "2. 1 та маҳсулот ўйлаб топ\n"
        "3. 10 та клиент топ\n"
        "4. Ҳар бирига ёз\n"
        "5. Натижани таҳлил қил"
    )

# ================= SELL =================
@dp.message(Command("sell"))
async def sell(message: types.Message):
    products = [
        "PDF / чек-лист",
        "Telegram бот хизмат",
        "Контент режа",
        "Excel шаблон",
        "Mini курс"
    ]
    await message.answer(f"💰 Сотиш учун:\n{random.choice(products)}")

# ================= DEFAULT =================
@dp.message()
async def default(message: types.Message):
    await message.answer(
        "Мен AI агентман 😎\n\n"
        "Командалар:\n"
        "/idea\n"
        "/niche\n"
        "/plan\n"
        "/sell"
    )

# ================= RUN =================
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
