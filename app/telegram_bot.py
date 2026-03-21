import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from app.agent import run_agent

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

user_state = {}


async def send_long_message(message: types.Message, text: str, chunk_size: int = 4000):
    for i in range(0, len(text), chunk_size):
        await message.answer(text[i:i + chunk_size])


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔥 WOLF AI AGENT\n\n"
        "Командалар:\n"
        "/hunt - имконият топ\n"
        "/ask савол бер\n"
        "/startwork - агент режими\n"
        "/leads ниша - клиент типларини топ\n"
        "/pitch текст - тайёр ёзиш матни\n"
        "/auto ниша - lead + message тайёр\n\n"
        "Мисоллар:\n"
        "/hunt\n"
        "/ask менга 0$ дан хизмат сотишни ўргат\n"
        "/leads short-form video editing\n"
        "/pitch TikTok блогер, subtitle yo‘q\n"
        "/auto video editing"
    )


@dp.message(Command("hunt"))
async def hunt(message: types.Message):
    prompt = """
Bugungi kunda internetda qonuniy ravishda tezroq pul topish mumkin bo‘lgan 5 ta yo‘lni ber.
Har biri uchun:
- nima o‘zi
- kimga mos
- qanday boshlanadi
- birinchi pul qayerdan keladi
Qisqa va konkret yoz.
"""
    result = run_agent(prompt)
    await send_long_message(message, "🧭 HUNT:\n\n" + result)


@dp.message(Command("ask"))
async def ask(message: types.Message):
    text = message.text.replace("/ask", "", 1).strip()
    if not text:
        await message.answer("Савол ёз. Масалан:\n/ask менга 0$ билан хизмат сотиш планини бер")
        return

    result = run_agent(text)
    await send_long_message(message, "🤖 JAVOB:\n\n" + result)


@dp.message(Command("leads"))
async def leads(message: types.Message):
    niche = message.text.replace("/leads", "", 1).strip() or "short-form video editing"

    prompt = f"""
Sen global lead finder san.

Niche: {niche}

10 ta potensial klient tipini ber.
Har biri uchun yoz:
1. Platforma
2. Kim o‘zi
3. Ularning muammosi
4. Biz ularga nima taklif qilamiz

Juda konkret yoz.
"""
    result = run_agent(prompt)
    await send_long_message(message, "🕵️ LEADS:\n\n" + result)


@dp.message(Command("pitch"))
async def pitch(message: types.Message):
    text = message.text.replace("/pitch", "", 1).strip()
    if not text:
        await message.answer(
            "Текст ёз. Масалан:\n"
            "/pitch TikTok блогер, видеоларида subtitle yo‘q, reelslari sust"
        )
        return

    prompt = f"""
Quyidagi klient uchun qisqa va kuchli outreach yoz:

{text}

Talab:
- 2-4 gap
- hook + value + soft CTA
- tabiiy yoz
- juda qattiq sotuvchi bo‘lma
- ingliz tilida yoz
"""
    result = run_agent(prompt)
    await send_long_message(message, "💬 PITCH:\n\n" + result)


@dp.message(Command("auto"))
async def auto_mode(message: types.Message):
    niche = message.text.replace("/auto", "", 1).strip()
    if not niche:
        await message.answer("Масалан:\n/auto video editing")
        return

    prompt = f"""
Niche: {niche}

5 ta real klient turi ber va har biri uchun outreach yoz.

Format:
1. Kim
Platforma:
Muammo:
Taklif:
Message:
...
"""
    result = run_agent(prompt)
    await send_long_message(message, "🤖 AUTO MODE:\n\n" + result)


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
    text = (message.text or "").strip()

    if uid in user_state:
        step = user_state[uid]["step"]

        if step == 1:
            user_state[uid]["type"] = text
            user_state[uid]["step"] = 2
            await message.answer("2-qadam:\nMaqsad yoz (масалан: 7 kunda 100$)")
            return

        if step == 2:
            user_state[uid]["goal"] = text
            user_state[uid]["step"] = 3
            await message.answer("3-qadam:\nBudjet yoz (0$, 50$, 200$)")
            return

        if step == 3:
            user_state[uid]["budget"] = text

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

Javob amaliy bo‘lsin.
"""
            result = run_agent(prompt)
            await send_long_message(message, "🔥 STRATEGIYA:\n\n" + result)

            del user_state[uid]
            return

    if text.startswith("/"):
        await message.answer("Буйруқ топилмади. /start ни босиб менюни кўр.")
        return

    result = run_agent(text)
    await send_long_message(message, result)
