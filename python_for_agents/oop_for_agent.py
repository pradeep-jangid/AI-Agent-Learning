class BaseAgent:
    def __init__(self, name: str, model: str = "gpt-4o-mini"):
        self.name = name
        self.model = model
    
    def run(self, task: str) -> str:
        return f"{self.name} processing: {task}"

class ResearchAgent(BaseAgent):
    def search(self, query: str) -> str:
        return f"Searching: {query}"

class WriterAgent(BaseAgent):
    def write(self, topic: str) -> str:
        return f"Writing about: {topic}"

r = ResearchAgent("Scholar", "claude-sonnet-4-20250514")
print(r.name)          # Scholar (from BaseAgent)
print(r.search("AI"))  # Searching: AI (own method)
print(r.run("AI"))