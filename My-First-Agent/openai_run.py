from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',  # Ollama endpoint
    api_key='ollama'                        # dummy, required but unused
)
response = client.chat.completions.create(
    model='llama3.2',
    messages=[{'role': 'user', 'content': """What's your name"""}]
)
print(response.choices)
