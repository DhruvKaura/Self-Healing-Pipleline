from ollama import chat

response = chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print(response["message"]["content"])