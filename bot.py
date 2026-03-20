user_states = {}

@dp.message(Command("startwork"))
async def start_work(message: types.Message):
    user_states[message.from_user.id] = 1
    await message.answer(
        "🔥 AGENT MODE БОШЛАНДИ\n\n"
        "1-қадам:\n"
        "👉 Битта ниша танла (AI / бизнес / савдо)\n\n"
        "Танлаб бўлсан → 'done' деб ёз"
    )

@dp.message()
async def agent_flow(message: types.Message):
    user_id = message.from_user.id

    if user_id not in user_states:
        return

    step = user_states[user_id]
    text = message.text.lower()

    if text != "done":
        await message.answer("❗ Тугатсан → 'done' деб ёз")
        return

    if step == 1:
        user_states[user_id] = 2
        await message.answer(
            "2-қадам:\n"
            "👉 Қандай маҳсулот сотасан?\n"
            "(PDF / бот / хизмат)\n\n"
            "Танлаб → done"
        )

    elif step == 2:
        user_states[user_id] = 3
        await message.answer(
            "3-қадам:\n"
            "👉 10 та потенциал клиент топ\n"
            "(Telegram / Instagram)\n\n"
            "Қилиб → done"
        )

    elif step == 3:
        user_states[user_id] = 4
        await message.answer(
            "4-қадам:\n"
            "👉 Уларга ёзиш:\n"
            "‘Сизга бот/хизмат керакми?’\n\n"
            "Ёзиб → done"
        )

    elif step == 4:
        user_states[user_id] = 5
        await message.answer(
            "🔥 5-қадам:\n"
            "👉 Жавобларни анализ қил\n"
            "👉 Ким қизиқди — шунга босим бер\n\n"
            "DONE → сен иш бошладинг 😎"
        )
