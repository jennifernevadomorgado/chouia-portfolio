# Les trois rôles

## Rôle 1 — Nouveaux tickets

- **Déclencheur** : webhook GLPI à la création d'un ticket.
- **Réponse** : un seul message, avec des étapes validées écrites par Python.
- **Sécurité** : si le problème ne correspond à aucun parcours validé, pas de réponse ; ticket déjà traité ignoré ; pendant les tests, seuls les tickets « [TEST CHATBOT] » de comptes autorisés sont traités.

## Rôle 2 — Utilisateur dans le chat

- **Parcours guidés** écrits à l'avance et suivis par Python : wifi, mot de passe, messagerie, écran noir, PC lent, imprimante…
- **Une question à la fois**, langage simple, même qualité en français et en néerlandais (règle FR = NL vérifiée automatiquement).
- **Ticket** : si le problème continue, Python prépare un résumé clair et le montre à l'utilisateur ; le ticket n'est créé qu'après son « oui ».

## Rôle 3 — Technicien

- Ouvert depuis la page d'un ticket.
- **Aide** : résumé, anciens tickets semblables, manuels officiels, procédures internes, internet (sites officiels et forums).
- **Traduction** : prépare la réponse du technicien en néerlandais pour un demandeur néerlandophone ; le technicien relit et envoie lui-même.
- **Garde-fous** : opérations risquées signalées, jamais de modification du ticket.

## Sources par rôle

| Source | Rôle 1 | Rôle 2 | Rôle 3 |
|---|---|---|---|
| Parcours validés | ✔ | ✔ | — |
| Anciens tickets (masqués) | — | — | ✔ |
| Manuels d'équipement | propositions | ✔ | ✔ |
| Documents internes | — | documents « utilisateurs » | tous les documents validés |
| Internet | sites officiels | sites officiels | sites officiels + forums |
