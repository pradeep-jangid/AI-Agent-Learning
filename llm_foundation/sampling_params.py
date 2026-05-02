import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def chat(
    prompt: str,
    model: str = "gemini-2.5-flash",
    temperature: float = 0.7,
    # top_p: float = 0.9,
    # seed: int = 42,
    max_tokens: int = 1000,
    system: str = "You are a helpful assistant.",
) -> str:
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=temperature,
            # top_p=top_p,
            # seed=seed,
            max_output_tokens=max_tokens,
        ),
    )
    return response.text


if __name__ == "__main__":
    # deterministic — same seed = same output
    result = chat("Name a flavor nobody has invented yet", temperature=0.1)
    print("deterministic:", result)

    # creative — high temp, no seed
    result = chat("Name a flavor nobody has invented yet", temperature=1.8)
    print("creative:", result)
