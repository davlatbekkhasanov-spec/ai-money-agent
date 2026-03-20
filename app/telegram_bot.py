from aiogram import F

user_state = {}

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
        "- digital\n"
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
        User:
        Yo‘nalish: {user_state[uid]['type']}
        Maqsad: {user_state[uid]['goal']}
        Budjet: {user_state[uid]['budget']}

        Shu user uchun real pul topish strategiya ber:
        - konkret qadamlar
        - qayerdan boshlash
        - qayerdan pul keladi
        """

        result = run_agent(prompt)
        await message.answer("🔥 STRATEGIYA:\n\n" + result[:4000])

        del user_state[uid]
