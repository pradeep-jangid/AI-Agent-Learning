import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Explain AI agents'}]
)
print(response['message']['content'])
