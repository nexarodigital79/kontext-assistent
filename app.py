import os
import requests

antwort = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},
    json={
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": "Erklaere RAG in zwei Saetzen."}
        ],
    },
)

daten = antwort.json()
print(daten["choices"][0]["message"]["content"])