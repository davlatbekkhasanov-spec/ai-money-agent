import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY topilmadi")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
client = OpenAI(api_key=OPENAI_API_KEY)

user_states = {}

SYSTEM_PROMPT = """
Sen kuchli AI biznes-agent san.
Vazifang:
- internetda qonuniy va real pul topish yo‘llarini topish
- foydalanuvchiga chuqur, amaliy, bosqichma-bosqich plan berish
- global fikrlash: AQSH, Yevropa, Osiyo, Yaqin Sharq va boshqa bozorlarda ishlaydigan modellarni tushuntirish
- lekin firibgarlik, spam, account o‘g‘irlash, noqonuniy sxema, "oson boyish" yolg‘onlarini tavsiya qilma

Javob formati:
1. Eng kuchli variantlar
2. Qaysi biri tez start
3. Qaysi biri ko‘p kapital talab qiladi
4. 7 kunlik plan
5. 30 kunlik plan
6. Kerak bo‘lsa sotuv matni va content idea
Javoblar kuchli, uzun, amaliy bo‘lsin.
"""

def ask_ai(user_prompt: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.output_text

async def send_long_message(message: types.Message, text: str, chunk_size: int = 4000):
    for i in range(0, len(text), chunk_size):
        await message.answer(text[i:i + chunk_size])

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "🔥 AI MONEY AGENT PRO MAX\n\n"
        "Buyruqlar:\n"
        "/idea - kuchli pul topish g‘oyasi\n"
        "/niche - global niche tahlili\n"
        "/plan - 30 kunlik plan\n"
        "/ask savol - istalgan savol ber\n"
        "/startwork - agent rejimini boshlash\n\n"
        "Masalan:\n"
        "/ask menga 0 dan 1000$ gacha chiqish strategiyasi ber"
    )

@dp.message(Command("idea"))
async def idea_cmd(message: types.Message):
    prompt = """
    Menga internetda qonuniy pul topish uchun eng kuchli 10 ta yo‘nalishni ber.
    Har biri bo‘yicha:
    - nima o‘zi
    - qaysi davlatlarda yaxshi ishlaydi
    - boshlash oson yoki qiyin
    - taxminiy daromad modeli
    """
    text = ask_ai(prompt)
    await send_long_message(message, text)

@dp.message(Command("niche"))
async def niche_cmd(message: types.Message):
    prompt = """
    Hozirgi davr uchun global bozorda eng istiqbolli 15 ta niche ber.
    Ularni quyidagicha ajrat:
    - tez pul
    - uzoq muddatli katta biznes
    - kam budjet bilan boshlanadigan
    - AI bilan birga qilsa bo‘ladigan
    """
    text = ask_ai(prompt)
    await send_long_message(message, text)

@dp.message(Command("plan"))
async def plan_cmd(message: types.Message):
    prompt = """
    Menga internetda pul topish uchun 30 kunlik juda kuchli plan tuz.
    Plan:
    - 1-7 kun
    - 8-14 kun
    - 15-21 kun
    - 22-30 kun
    Va har bosqichda aniq nima qilishimni yoz.
    """
    text = ask_ai(prompt)
    await send_long_message(message, text)

@dp.message(Command("ask"))
async def ask_cmd(message: types.Message):
    user_text = message.text.replace("/ask", "", 1).strip()
    if not user_text:
        await message.answer("Savol yoz. Masalan:\n/ask menga affiliate marketingni 0 dan o‘rgat")
        return

    text = ask_ai(user_text)
    await send_long_message(message, text)

@dp.message(Command("startwork"))
async def start_work(message: types.Message):
    user_states[message.from_user.id] = 1
    await message.answer(
        "🔥 AGENT MODE BOSHLANDI\n\n"
        "1-qadam:\n"
        "Bitta yo‘nalish tanla:\n"
        "- affiliate\n"
        "- digital product\n"
        "- service\n"
        "- content\n\n"
        "Tanlab bo‘lsang, shu yerga yoz."
    )

@dp.message()
async def agent_flow(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip()

    if user_id in user_states:
        step = user_states[user_id]

        if step == 1:
            user_states[user_id] = 2
            await message.answer(
                f"Zo‘r. Sen tanlading: {text}\n\n"
                "2-qadam:\n"
                "Endi maqsadni yoz:\n"
                "Masalan: 30 kunda 300$"
            )
            return

        elif step == 2:
            user_states[user_id] = 3
            await message.answer(
                f"Maqsad qabul qilindi: {text}\n\n"
                "3-qadam:\n"
                "Budjetingni yoz:\n"
                "Masalan: 0$, 50$, 200$"
            )
            return

        elif step == 3:
            goal_prompt = (
                "Foydalanuvchi uchun shaxsiy action-plan tuz.\n"
                f"Yo‘nalish: oldingi tanlov bor.\n"
                f"Budjet: {text}\n"
                "Juda amaliy, bosqichma-bosqich plan ber.\n"
                "Format:\n"
                "1. Eng yaxshi model\n"
                "2. 7 kunlik reja\n"
                "3. 30 kunlik reja\n"
                "4. Birinchi sotuvni qanday olish\n"
            )
            user_states.pop(user_id, None)
            ai_text = ask_ai(goal_prompt)
            await send_long_message(message, "🔥 Shaxsiy agent planning tayyor:\n\n" + ai_text)
            return

    text_lower = text.lower()

    if text_lower.startswith("/"):
        await message.answer("Buyruq topilmadi. /start ni bosib menyuni ko‘r.")
        return

    ai_text = ask_ai(
        f"Foydalanuvchi savoli: {text}\n"
        "Shunga kuchli, amaliy va uzun javob ber."
    )
    await send_long_message(message, ai_text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
