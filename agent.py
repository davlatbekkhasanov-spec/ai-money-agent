from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM = """
Sen professional AI business agent san.

Vazifang:
- global internet pul topish imkoniyatlarini topish
- real va qonuniy yo‘llar berish
- tez pul va uzoq muddatli strategiyani ajratish
- foydalanuvchini majbur qiladigan action-plan berish

Javob:
- konkret
- agressiv
- amaliy
"""

def run_agent(user_input: str):
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user_input},
        ],
    )
    return response.output_text
