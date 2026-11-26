"""Recherche par le sens dans ChromaDB (RAG), avec des embeddings bge-m3 via Ollama.

Exemple réécrit pour le portfolio, avec des données fictives.
"""
import chromadb
import requests


def embedding(texte: str) -> list[float]:
    r = requests.post("http://localhost:11434/api/embeddings",
                      json={"model": "bge-m3", "prompt": texte}, timeout=60)
    r.raise_for_status()
    return r.json()["embedding"]


client = chromadb.PersistentClient(path="./base_exemple")
collection = client.get_or_create_collection("tickets_exemple")

# Données fictives, déjà masquées
tickets = {
    "t1": "Imprimante bloquée : [utilisateur] signale un bourrage papier, résolu en ouvrant le tiroir 2.",
    "t2": "Outlook ne s'ouvre plus : profil réparé depuis le panneau de configuration.",
    "t3": "Wifi déconnecté : oubli du réseau puis reconnexion avec le compte.",
}
collection.upsert(ids=list(tickets), documents=list(tickets.values()),
                  embeddings=[embedding(t) for t in tickets.values()])


def chercher(question: str, n: int = 2, distance_max: float = 0.6) -> list[str]:
    res = collection.query(query_embeddings=[embedding(question)], n_results=n)
    # On ne garde que les passages assez proches : mieux vaut rien qu'un mauvais exemple
    return [doc for doc, d in zip(res["documents"][0], res["distances"][0]) if d <= distance_max]


if __name__ == "__main__":
    print(chercher("le papier est coincé dans l'imprimante"))
