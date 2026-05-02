# AI Agent Learning Journey

A hands-on repo documenting my path from zero to building AI agents — experimenting with OpenAI, Google Gemini, Ollama (local), and Anthropic.

---

## Roadmap

- [x] **Phase 1** — First API calls (OpenAI, Gemini, Ollama)
- [x] **Phase 2** — Local models with Ollama + custom Modelfile
- [ ] **Phase 3** — Tool use & function calling
- [ ] **Phase 4** — Memory & context management
- [ ] **Phase 5** — Multi-agent systems
- [ ] **Phase 6** — Production-ready agent with LangChain

---

## Project Structure

```
AI-Agent-Learning/
├── My-First-Agent/
│   ├── openai_first_call.py     # First OpenAI API call (gpt-4o-mini)
│   ├── openai_run.py            # OpenAI-compatible call to local Ollama
│   ├── gemini_first_api_call.py # First Gemini API call (gemini-2.5-flash)
│   ├── ollama_ran.py            # Local LLM via Ollama Python SDK
│   └── Modelfile                # Custom Ollama model — AI tutor persona
├── agent_python/
│   ├── oop_for_agent.py         # OOP patterns for agents (BaseAgent class)
│   ├── my_pydantic.py           # Pydantic models for tool calls & structured output
│   ├── demo_asyncio.py          # Async LLM calls with asyncio
│   └── mini_llm_project/
│       └── call_gemini_model.py # Async Gemini calls
├── pyproject.toml               # Dependencies (uv)
├── .python-version              # Python 3.12
└── .env                         # API keys (not committed)
```

---

## Phase 1 — First API Calls

### OpenAI (`openai_first_call.py`)
```python
client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is an AI Agent in 2 lines?"}]
)
```
Key learnings: API key auth, chat message format, `temperature`, `max_tokens`.

### Google Gemini (`gemini_first_api_call.py`)
```python
genai.GenerativeModel("gemini-2.5-flash", system_instruction="...")
model.generate_content("...", generation_config=GenerationConfig(...))
```
Key learnings: Gemini SDK differs from OpenAI — system prompt passed at model init, not in messages.

---

## Phase 2.5 — Python Fundamentals for Agents (`agent_python/`)

### OOP for Agents (`oop_for_agent.py`)
```python
class BaseAgent:
    def __init__(self, name: str, model: str = "gpt-4o-mini"):
        ...
```
Key learnings: Agent as a class, encapsulating model + name, foundation for multi-agent systems.

### Pydantic for Structured Output (`my_pydantic.py`)
```python
class ToolCall(BaseModel):
    name: str = Field(description="Tool name")
```
Key learnings: Validate LLM responses with Pydantic — ensures structured tool call parsing.

### Async LLM Calls (`demo_asyncio.py`, `mini_llm_project/call_gemini_model.py`)
```python
async def call_llm(model: str, sleep_time: int) -> str: ...
await asyncio.gather(call_llm("gpt-4o"), call_llm("gemini"))
```
Key learnings: `asyncio.gather` runs multiple LLM calls concurrently — critical for agent parallelism.

---

## Phase 2 — Local Models with Ollama

### Ollama Python SDK (`ollama_ran.py`)
```python
ollama.chat(model='llama3.2', messages=[...])
```

### Ollama via OpenAI-compatible API (`openai_run.py`)
```python
OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
```
Key learnings: Ollama exposes an OpenAI-compatible endpoint — swap `base_url`, keep same code.

### Custom Modelfile
```
FROM llama3.2
SYSTEM """You are an AI agent development tutor..."""
PARAMETER temperature 0.7
PARAMETER num_ctx 8192
```
Key learnings: `Modelfile` creates a custom local model persona via `ollama create`.

---

## Setup

**Prerequisites:** Python 3.12+, [uv](https://github.com/astral-sh/uv), [Ollama](https://ollama.com)

```bash
# Install dependencies
uv sync

# Pull local model
ollama pull llama3.2

# Create custom tutor model
ollama create ai-tutor -f My-First-Agent/Modelfile

# Copy and fill env
cp .env.example .env
```

`.env` format:
```
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=AIza...
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `openai` | OpenAI + Ollama OpenAI-compat API |
| `google-generativeai` | Gemini API |
| `ollama` | Local models via Ollama |
| `anthropic` | Claude API (Phase 3+) |
| `langchain` | Agent framework (Phase 6) |
| `pydantic` | Data validation |
| `python-dotenv` | Env var loading |

---

## Key Concepts Learned

| Concept | Where |
|---|---|
| Chat completions format | `openai_first_call.py` |
| System prompts | `openai_first_call.py`, `gemini_first_api_call.py` |
| Local LLM inference | `ollama_ran.py` |
| OpenAI-compatible endpoints | `openai_run.py` |
| Custom model personas | `Modelfile` |
| OOP agent design | `agent_python/oop_for_agent.py` |
| Pydantic structured output | `agent_python/my_pydantic.py` |
| Async concurrent LLM calls | `agent_python/demo_asyncio.py` |
