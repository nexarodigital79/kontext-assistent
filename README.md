# kontext-assistent

Kleines Python-Skript, das eine Frage **ausschließlich anhand eines fest vorgegebenen Kontext-Textes** beantwortet — kein allgemeines Modellwissen, reines Context Engineering (noch ohne RAG/Retrieval). Erstes Portfolio-Projekt (P1) im Rahmen meiner AI-Engineer-Lernroadmap.

## Was macht das Skript?

`app.py` baut aus einem festen Kontext-Satz und einer Frage einen gemeinsamen Prompt und schickt ihn an eine LLM-Chat-API. Die Antwort wird ausschließlich aus dem mitgegebenen Kontext abgeleitet, nicht aus dem Trainingswissen des Modells — getestet mit einer bewusst erfundenen Tatsache im Kontext-Text, auf die das Modell korrekt geantwortet hat.

Enthält außerdem einfache Fehlerbehandlung: Antwortet die API mit einem Fehler (z. B. falscher Modellname), gibt das Skript kontrolliert `fehler` aus, statt mit einem `KeyError` abzustürzen.

## Provider-Wahl

Aktuell wird [Groq](https://groq.com) (Modell `openai/gpt-oss-120b`) über eine OpenAI-kompatible Chat-Completions-API angesprochen — kostenlos nutzbar, für diese Größenordnung an Aufgabe (Frage anhand kurzem Text beantworten) ausreichend. Der Provider ist bewusst nicht festgelegt: Requests-Aufbau, Header und Antwortstruktur sind bei den meisten LLM-Anbietern (u. a. Anthropic Claude) nahezu identisch, ein Wechsel würde im Kern nur URL, Modellname und API-Key betreffen.

## Voraussetzungen

- Python 3
- Paket `requests` (`pip install requests`)
- Umgebungsvariable `GROQ_API_KEY` mit einem gültigen Groq-API-Key ([console.groq.com](https://console.groq.com))

## Nutzung

```powershell
$env:GROQ_API_KEY = "dein-key-hier"
python app.py
```

Das Skript gibt die Antwort des Modells auf der Konsole aus.

## Stand

- Kontext-Grounding funktioniert (verifiziert)
- Fehlerbehandlung vorhanden (if/else gegen `KeyError` bei Fehlerantworten)
- `.gitignore` schützt `.env` und `__pycache__/` vor versehentlichem Commit

