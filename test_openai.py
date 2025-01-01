import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("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")

prompt = "Hello, how can I assist you today?"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text

print("Response:", generate_response(prompt))
