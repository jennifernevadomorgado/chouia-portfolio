"""API minimale inspirée de Chouia : clé obligatoire, puis choix du rôle.

Exemple réécrit et simplifié pour le portfolio (pas le code de production).
Lancer : uvicorn api_minimale:app --reload
"""
import os
import secrets

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

API_KEY = os.environ.get("API_KEY", "")  # jamais écrite dans le code
ROLES_ACTIFS = {"user", "technician"}

app = FastAPI(title="Assistant GLPI (exemple)")


class Demande(BaseModel):
    role: str
    question: str = Field(min_length=1, max_length=2000)
    ticket_id: int | None = None  # seulement pour le rôle technicien


def verifier_cle(cle: str | None) -> None:
    # compare_digest évite de révéler la clé par le temps de réponse
    if not API_KEY or not cle or not secrets.compare_digest(cle, API_KEY):
        raise HTTPException(status_code=401, detail="Clé invalide")


@app.post("/chat")
def chat(demande: Demande, x_api_key: str | None = Header(default=None)):
    verifier_cle(x_api_key)
    if demande.role not in ROLES_ACTIFS:
        raise HTTPException(status_code=400, detail="Rôle inconnu ou désactivé")
    if demande.role == "technician" and demande.ticket_id is None:
        raise HTTPException(status_code=400, detail="Numéro de ticket requis")

    # Dans le vrai projet : filtre de sécurité → recherche → modèle → contrôle
    return {"role": demande.role, "reponse": f"(exemple) Question reçue : {demande.question}"}
