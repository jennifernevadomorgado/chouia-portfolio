"""Masquage des noms de personnes avant l'indexation (spaCy FR / NL).

Exemple réécrit pour le portfolio.
Installation : pip install spacy && python -m spacy download fr_core_news_md nl_core_news_md
"""
import re

import spacy

MODELES = {"fr": spacy.load("fr_core_news_md"), "nl": spacy.load("nl_core_news_md")}
MASQUE = "[utilisateur]"


def masquer(texte: str, langue: str = "fr", noms_connus: list[str] | None = None) -> str:
    # 1. Noms connus (personnes liées au ticket, membres du service) : remplacement sûr
    for nom in sorted(noms_connus or [], key=len, reverse=True):
        texte = re.sub(rf"\b{re.escape(nom)}\b", MASQUE, texte, flags=re.IGNORECASE)
    # 2. spaCy repère les autres noms de personnes (entités PER)
    doc = MODELES[langue](texte)
    for ent in reversed(doc.ents):
        if ent.label_ in ("PER", "PERSON"):
            texte = texte[:ent.start_char] + MASQUE + texte[ent.end_char:]
    return texte


if __name__ == "__main__":
    print(masquer("Marie Dupont ne reçoit plus ses mails, Paul Martin a vérifié.", "fr", ["Paul Martin"]))
