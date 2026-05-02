import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Strawberry"
tokens = enc.encode(text)
print(f"Tokens: {len(tokens)}")  # 6
print([enc.decode([t]) for t in tokens])
# ['AI', ' Agents', ' are', ' the', ' future']
