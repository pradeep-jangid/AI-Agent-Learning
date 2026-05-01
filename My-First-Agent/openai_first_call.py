from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()  # auto-reads OPENAI_API_KEY

response = client.chat.completions.create(
    model="gpt-4o-mini",       # cheapest model
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor"},
        {"role": "user", "content": "What is an AI Agent in 2 lines?"}
    ],
    temperature=0.7,
    max_tokens=200
)

print(response.choices[0].message.content)