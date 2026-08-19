# os liest Umgebungsvariablen (den API-Key), requests schickt den HTTP-Request
import os
import requests

# POST-Request an die Groq-Chat-API: URL, Auth-Header mit Bearer-Token aus der
# Umgebungsvariable GROQ_API_KEY, und der JSON-Body mit Modellname + der
# eigentlichen Frage als "messages"-Liste (Chat-Format, auch bei nur einer Nachricht)
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

# Antwort-Body von JSON in ein Python-dict parsen
daten = antwort.json()
# choices[0] = erste (und einzige) Antwortoption, message.content = der Text darin
print(daten["choices"][0]["message"]["content"])