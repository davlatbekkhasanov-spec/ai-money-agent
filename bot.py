import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================= START =================
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔥 AI MONEY AGENT PRO\n\n"
        "Командалар:\n"
        "/idea - кучли бизнес ғоя\n"
        "/niche - чуқур ниша анализ\n"
        "/plan - босқичма-босқич план\n"
        "/sell - сотиш стратегияси\n"
    )

# ================= IDEA =================
@dp.message(Command("idea"))
async def idea(message: types.Message):
    await message.answer(
        "💡 КУЧЛИ ҒОЯ:\n\n"
        "👉 Telegram канал: 'Пул топиш ва бизнес'\n\n"
        "Қандай ишлайди:\n"
        "- Кунига 2-3 пост (қисқа, фойдали)\n"
        "- Контент: реал кейслар, лайфхаклар\n"
        "- 7-10 кунда аудитория йиғилади\n\n"
        "Монетизация:\n"
        "- PDF (30-100 мин сўм)\n"
        "- Реклама\n"
        "- Консультация\n\n"
        "🔥 Бу модел Ўзбекистонда ишлайди"
    )

# ================= NICHE =================
@dp.message(Command("niche"))
async def niche(message: types.Message):
    await message.answer(
        "📊 НИША АНАЛИЗ:\n\n"
        "1. 💰 Пул топиш / бизнес\n"
        "   - Катта талаб\n"
        "   - Осон сотилади\n"
        "   - Минус: рақобат юқори\n\n"
        "2. 🤖 AI ва технология\n"
        "   - Хайпда\n"
        "   - Контент тез ўсади\n"
        "   - Минус: тушунтириш керак\n\n"
        "3. 🛒 Онлайн савдо\n"
        "   - Реал пул\n"
        "   - Клиентлар бор\n"
        "   - Минус: ишлаш керак\n\n"
        "👉 ТАВСИЯ: AI + пул топиш аралаш ниша 🔥"
    )

# ================= PLAN =================
@dp.message(Command("plan"))
async def plan(message: types.Message):
    await message.answer(
        "📅 7 КУНЛИК РЕАЛ ПЛАН:\n\n"
        "1-КУН:\n"
        "- Ниша танла\n"
        "- Telegram канал оч\n\n"
        "2-КУН:\n"
        "- 5 та пост ёз\n"
        "- Дизайн қўш\n\n"
        "3-КУН:\n"
        "- 10 та каналга реклама бер\n"
        "- 100 та одам йиғ\n\n"
        "4-КУН:\n"
        "- PDF маҳсулот тайёрла\n"
        "- Нарх қўй\n\n"
        "5-КУН:\n"
        "- Контент давом эт\n"
        "- Сотув бошла\n\n"
        "6-КУН:\n"
        "- Клиентлар билан ишла\n"
        "- Фикр йиғ\n\n"
        "7-КУН:\n"
        "- Анализ қил\n"
        "- Масштаб қил 🔥"
    )

# ================= SELL =================
@dp.message(Command("sell"))
async def sell(message: types.Message):
    await message.answer(
        "💰 СОТИШ СТРАТЕГИЯСИ:\n\n"
        "1. Арзон маҳсулот (20-50 мин)\n"
        "2. Қиммат версия (100-300 мин)\n"
        "3. Limited оффер:\n"
        "   'Фақат 24 соат'\n\n"
        "4. Контент орқали қизиқтир:\n"
        "- кейс\n"
        "- натижа\n"
        "- фойда\n\n"
        "👉 Формула:\n"
        "Контент → Қизиқиш → Сотув"
    )

# ================= DEFAULT =================
@dp.message()
async def default(message: types.Message):
    await message.answer(
        "Мен PRO AI агентман 😎\n"
        "/idea /niche /plan /sell"
    )

# ================= RUN =================
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
