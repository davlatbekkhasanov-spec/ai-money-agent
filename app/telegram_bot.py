from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

from app.agent import run_agent

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

user_state = {}


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔥 WOLF AI AGENT\n\n"
        "/hunt - imkoniyat top\n"
        "/ask savol ber\n"
        "/startwork - agent rejimi\n"
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


@dp.message(Command("startwork"))
async def startwork(message: types.Message):
    user_state[message.from_user.id] = {"step": 1}
    await message.answer(
        "🔥 AGENT MODE BOSHLANDI\n\n"
        "1-qadam:\n"
        "Yo‘nalish tanla:\n"
        "- affiliate\n"
        "- service\n"
        "- content\n"
        "- digital"
    )


@dp.message()
async def step_handler(message: types.Message):
    uid = message.from_user.id

    if uid not in user_state:
        result = run_agent(message.text)
        await message.answer(result[:4000])
        return

    step = user_state[uid]["step"]

    if step == 1:
        user_state[uid]["type"] = message.text
        user_state[uid]["step"] = 2
        await message.answer("2-qadam:\nMaqsad yoz (masalan: 7 kunda 100$)")
        return

    if step == 2:
        user_state[uid]["goal"] = message.text
        user_state[uid]["step"] = 3
        await message.answer("3-qadam:\nBudjet yoz (0$, 50$, 200$)")
        return

    if step == 3:
        user_state[uid]["budget"] = message.text

        prompt = f"""
Foydalanuvchi uchun real strategiya tuz.

Yo‘nalish: {user_state[uid]['type']}
Maqsad: {user_state[uid]['goal']}
Budjet: {user_state[uid]['budget']}

Javobda yoz:
1. Eng yaxshi model
2. 7 kunlik plan
3. 30 kunlik plan
4. Birinchi pulni qayerdan olish
5. Mijozga yozish uchun tayyor text
"""

        result = run_agent(prompt)
        await message.answer("🔥 STRATEGIYA:\n\n" + result[:4000])

        del user_state[uid]
