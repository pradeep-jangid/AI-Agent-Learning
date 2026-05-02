import os
import asyncio
from typing import Optional, List

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


class Query(BaseModel):
    question: str = Field(description="User question")


class Answer(BaseModel):
    response: str = Field(description="Answer text")
    confidence: float
    sources: List[str] = Field(default=[])
    follow_up: Optional[str] = None


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
async def ask(query: Query) -> Answer:
    resp = await client.aio.models.generate_content(
        model="gemini-2.0-flash",
        contents=query.question,
        config=types.GenerateContentConfig(
            system_instruction="Return JSON with fields: response, confidence, sources, follow_up",
            response_mime_type="application/json",
            response_schema=Answer,
        ),
    )
    return Answer.model_validate_json(resp.text)


result = asyncio.run(ask(Query(question="What is an AI Agent?")))
print(result.response)
