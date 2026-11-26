# Sécurité et données personnelles

## Principes

- **Modèle local** : les conversations ne quittent pas le serveur.
- **Secrets hors du code** : clés et adresses dans un fichier `.env` (droits 600), jamais dans Git. Un crochet pre-commit bloque l'envoi de fichiers sensibles.
- **Accès à l'API** : chaque appel doit présenter une clé ; mauvaise clé → `401`.
- **GLPI** : compte technique aux droits limités ; écriture désactivée par défaut (interrupteur).
- **Limites de charge** : nombre de messages par minute et par utilisateur, nombre de réponses simultanées du modèle.

## Filtre des demandes dangereuses

Avant le modèle, Python refuse les demandes qui pourraient compromettre un poste, un compte ou des données (mot de passe administrateur, contournement de sécurité, suppression de données…), en français et en néerlandais.

## Masquage des noms

Les anciens tickets sont nettoyés avant l'indexation :
1. **Par listes** : personnes liées au ticket et membres du service.
2. **Par spaCy** (modèles FR et NL) : noms de personnes restants.

Les noms sont remplacés par `[utilisateur]`. Contrôle après masquage sur des tickets tirés au hasard.

## Internet

La recherche passe par SearXNG avec une requête technique filtrée par Python et une liste de sites autorisés. Ce filtrage réduit les données envoyées, sans garantie absolue d'anonymat : c'est documenté comme une limite.
