import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Sen professional AI business agent san.

Vazifang:
- internetda qonuniy va real pul topish yo‘llarini topish
- foydalanuvchiga amaliy, bosqichma-bosqich plan berish
- tez pul va uzoq muddatli strategiyani ajratish
- service, digital product, content, affiliate, lead generation yo‘nalishlarida yordam berish
- konkret va foydali javob berish

Muhim:
- firibgarlik, spam, account o‘g‘irlash, noqonuniy sxemalarni tavsiya qilma
- javoblar aniq va amaliy bo‘lsin
"""

def run_agent(user_input: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ],
    )
    return response.output_text
