# Tests

| Type | Ce qui est vérifié |
|---|---|
| Scénarios écrits à l'avance (FR et NL) | Les règles programmées : parcours, refus, langue, ticket |
| Rejeu automatique à chaque commit | 153 scénarios et 259 textes vérifiés |
| Simulations sur de vrais tickets, en lecture seule | La chaîne complète sur des cas réels, sans rien écrire |
| Tests en direct avec l'équipe informatique | Branchement au plugin, temps de réponse, comportement réel |

Une réponse non vide n'est jamais considérée comme « réussie » d'office : chaque réponse est classée **réussi / à revoir / échec** selon des critères définis.

## Leçons

- Tester très tôt avec la **vraie interface** : un blocage d'intégration (contrôle CSRF côté GLPI) n'est apparu qu'au branchement.
- Mesurer les temps de réponse sur le matériel réel : sans carte graphique, le modèle est le facteur limitant.
