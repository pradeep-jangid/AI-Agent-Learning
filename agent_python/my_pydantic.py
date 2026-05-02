from pydantic import BaseModel, Field
from typing import List, Optional

class ToolCall(BaseModel):
    name: str = Field(description="Tool name")
    arguments: dict = Field(description="Tool arguments")
    confidence: float = Field(ge=0, le=1)

class AgentResponse(BaseModel):
    thought: str = Field(description="Agent reasoning")
    tool_calls: List[ToolCall] = Field(default=[])
    final_answer: Optional[str] = None

# Validates automatically:
resp = AgentResponse(thought="Need search", tool_calls=[
    ToolCall(name="search", arguments={"q":"AI"}, confidence=1.7)
],final_answer="Found AI info")

print(resp)
