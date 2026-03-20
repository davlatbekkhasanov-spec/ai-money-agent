from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
from app.agent import run_agent

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔥 WOLF AI AGENT\n\n"
        "/hunt - imkoniyat top\n"
        "/ask savol ber\n"
    )

@dp.message(Command("hunt"))
async def hunt(message: types.Message):
    prompt = "Bugungi kunda internetda eng tez pul topish mumkin bo‘lgan 5 ta yo‘l ber"
    result = run_agent(prompt)
    await message.answer(result[:4000])

@dp.message(Command("ask"))
async def ask(message: types.Message):
    text = message.text.replace("/ask", "").strip()
    if not text:
        await message.answer("Savol yoz")
        return

    result = run_agent(text)
    await message.answer(result[:4000])

@dp.message()
async def default(message: types.Message):
    result = run_agent(message.text)
    await message.answer(result[:4000])
