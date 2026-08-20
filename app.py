# os liest Umgebungsvariablen (den API-Key), requests schickt den HTTP-Request
import os
import requests

# Fester Kontext-Text, aus dem das Modell die Antwort ausschliesslich ziehen soll
kontext = "es gibt 2 wege, der linke ist der richtige"
# Die Frage, die anhand des Kontexts beantwortet werden soll
frage = "welcher weg ist der richtige? der rechte?"
# Kontext und Frage zu einem einzigen Prompt zusammenbauen (f-String setzt die Variablen ein)
prompt = f"Kontext: {kontext}\n\nFrage: {frage}\n\nBeantworte NUR anhand des Kontexts."
# Anhang-C-Uebung 1 (Kontext-Vergleich, getestet): ohne diesen Kontext-Satz antwortete
# das Modell "der rechte" - falsch, und passend zur Suggestion in der Frage selbst
# ("der rechte?"). Mit Kontext antwortet es korrekt "der linke". Ob das echte
# Halluzination (erfundene Tatsache) oder nur Uebernahme der Frage-Suggestion war,
# ist aus diesem einen Test nicht sicher zu sagen - aber es zeigt klar: ohne Kontext
# hat das Modell keine verlaessliche Grundlage, sondern raet/uebernimmt Signale aus
# der Frage.

# POST-Request an die Groq-Chat-API: URL, Auth-Header mit Bearer-Token aus der
# Umgebungsvariable GROQ_API_KEY, und der JSON-Body mit Modellname + der
# eigentlichen Frage als "messages"-Liste (Chat-Format, auch bei nur einer Nachricht)
antwort = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={"Authorization": "Bearer " + os.environ["GROQ_API_KEY"]},
    json={
        # Anhang-C-Uebung 4 (Modell tauschen): 120b statt 20b, gleicher Anbieter Groq -
        # zeigt, dass ein Modellwechsel nur diesen einen String betrifft
        "model": "openai/gpt-oss-120b",
        "messages": [
            # Anhang-C-Uebung 2 (System-Rolle): eigene Nachricht VOR der User-Frage,
            # setzt einen generellen Ton/eine Regel fuers Modell (hier: Antwortsprache)
            {"role": "system", "content": "du antwortest auf englisch und bedankst dich auf deutsch am ende"},
            {"role": "user", "content": prompt}
        ],
    },
)
if antwort.status_code != 200:
    print("fehler")
else:
    # Antwort-Body von JSON in ein Python-dict parsen
    daten = antwort.json()
    # choices[0] = erste (und einzige) Antwortoption, message.content = der Text darin
    print(daten["choices"][0]["message"]["content"])
    # Anhang-C-Uebung 3 (Kosten sichtbar machen): "usage" zeigt Input-/Output-Token-
    # Verbrauch dieser einen Anfrage - Grundlage fuer die Kostenrechnung
    print(daten["usage"])
