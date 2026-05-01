import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",   # cheapest model
    system_instruction="You are a helpful AI tutor"
)

response = model.generate_content(
    "What is the AI Agent future in 2 lines?",
    generation_config=genai.GenerationConfig(
        temperature=0.1,
        max_output_tokens=200
    )
)

print(response.text)
