import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM = """
Sen professional AI business agent san.

Vazifang:
- internetda qonuniy va real pul topish yo‘llarini topish
- foydalanuvchiga amaliy, bosqichma-bosqich plan berish
- tez pul va uzoq muddatli strategiyani ajratish
- xizmat sotish, digital product, affiliate, content, lead generation yo‘nalishlarida yordam berish
- foydalanuvchiga konkret va foydali javob berish

Muhim:
- firibgarlik, spam, account o‘g‘irlash, noqonuniy sxemalarni tavsiya qilma
- javoblar aniq, qisqa bo‘lsa ham foydali bo‘lsin
- kerak bo‘lsa punktlar bilan yoz
"""

def run_agent(user_input: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user_input},
        ],
    )
    return response.output_text
