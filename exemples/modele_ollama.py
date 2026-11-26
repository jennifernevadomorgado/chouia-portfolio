"""Appel d'un modèle local avec Ollama, un modèle par langue.

Exemple réécrit pour le portfolio. Nécessite Ollama en local (http://localhost:11434).
"""
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODELES = {"fr": "qwen2.5:7b", "nl": "gemma3:12b"}  # choisis après essais comparatifs


def generer(langue: str, consigne: str, question: str, contexte: str = "") -> str:
    messages = [
        {"role": "system", "content": consigne},
        {"role": "system", "content": f"Informations utiles :\n{contexte}"} if contexte else None,
        {"role": "user", "content": question},
    ]
    reponse = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELES.get(langue, MODELES["fr"]),
            "messages": [m for m in messages if m],
            "stream": False,
            "options": {"temperature": 0.2, "num_predict": 400},
        },
        timeout=300,  # sur processeur, une réponse peut prendre plusieurs minutes
    )
    reponse.raise_for_status()
    return reponse.json()["message"]["content"].strip()


if __name__ == "__main__":
    print(generer("fr", "Tu es une assistante informatique. Réponds simplement.",
                  "Mon imprimante n'imprime plus, que faire ?"))
