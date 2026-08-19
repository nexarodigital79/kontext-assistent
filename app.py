# os liest Umgebungsvariablen (den API-Key), requests schickt den HTTP-Request
import os
import requests

# Fester Kontext-Text, aus dem das Modell die Antwort ausschliesslich ziehen soll
kontext = "es gibt 2 wege, der linke ist der richtige"
# Die Frage, die anhand des Kontexts beantwortet werden soll
frage = "welcher weg ist der richtige? der rechte?"
# Kontext und Frage zu einem einzigen Prompt zusammenbauen (f-String setzt die Variablen ein)
prompt = f"Kontext: {kontext}\n\nFrage: {frage}\n\nBeantworte NUR anhand des Kontexts."

# POST-Request an die Groq-Chat-API: URL, Auth-Header mit Bearer-Token aus der
# Umgebungsvariable GROQ_API_KEY, und der JSON-Body mit Modellname + der
# eigentlichen Frage als "messages"-Liste (Chat-Format, auch bei nur einer Nachricht)
antwort = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},
    json={
        "model": "openai/gpt-oss-20b",  # llama-3.3-70b-versatile ist deprecated, das hier ist aktuell
        "messages": [
            {"role": "user", "content": prompt}
        ],
    },
)

# Antwort-Body von JSON in ein Python-dict parsen
daten = antwort.json()
# choices[0] = erste (und einzige) Antwortoption, message.content = der Text darin
print(daten["choices"][0]["message"]["content"])
