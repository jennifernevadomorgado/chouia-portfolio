"""Filtre de sécurité appliqué AVANT le modèle (FR et NL).

Exemple réécrit et simplifié pour le portfolio.
"""
import re
import unicodedata

REGLES = [
    ("mot_de_passe_admin", r"mot de passe (admin|administrateur)|admin(istrator)?wachtwoord"),
    ("contournement", r"contourner|desactiver (l')?antivirus|omzeilen|antivirus uitschakelen"),
    ("suppression", r"supprimer (tous|toutes|le profil|les donnees)|alles verwijderen"),
]

REFUS = {
    "fr": "Je ne peux pas vous aider pour cette demande. Un technicien va prendre le relais si nécessaire.",
    "nl": "Ik kan u hiermee niet helpen. Een technicus neemt het indien nodig over.",
}


def normaliser(texte: str) -> str:
    sans_accents = unicodedata.normalize("NFD", texte)
    return "".join(c for c in sans_accents if unicodedata.category(c) != "Mn").lower()


def verifier(question: str, langue: str = "fr") -> tuple[bool, str | None]:
    """Renvoie (autorisé, message de refus éventuel)."""
    texte = normaliser(question)
    for nom, motif in REGLES:
        if re.search(motif, texte):
            return False, REFUS[langue]
    return True, None


if __name__ == "__main__":
    for q in ["Quel est le mot de passe administrateur ?", "Mon écran reste noir"]:
        print(q, "→", verifier(q))
