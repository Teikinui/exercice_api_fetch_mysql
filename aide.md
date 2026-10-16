# Aide — difficultés rencontrées

Ce fichier est le journal de progression. Chaque difficulté doit être ajoutée avec le contexte, la cause et l'indice de correction.

## Format à utiliser

### Exercice __ — Date : ____

- **Difficulté :**
- **Message d'erreur ou comportement observé :**
- **Cause identifiée :**
- **Indice :**
- **Correction appliquée :**
- **Ce que je retiens :**

---

## Rappels utiles

Cette section contient des rappels généraux. Les difficultés personnelles seront ajoutées au-dessus, exercice par exercice.

### React et état

- `useState` retourne une valeur et une fonction de mise à jour.
- Une réaffectation directe ne déclenche pas de nouveau rendu React.
- Un champ contrôlé a besoin de trois éléments : un état, `value={...}` et `onChange={...}`.
- `onClick={fonction}` transmet une fonction à React ; `onClick={fonction()}` exécute la fonction pendant le rendu.

### Listes React

- Chaque élément rendu par `map` doit avoir une `key` stable et unique.
- Pour supprimer un élément, passer explicitement son index ou son identifiant : `onClick={() => supprimer(id)}`.
- Utiliser `filter` ou une copie du tableau pour modifier une liste sans la muter directement.

### Fetch et API

- Vérifier `response.ok` avant d'utiliser les données.
- Une requête réseau doit gérer au minimum le chargement, le succès et l'erreur.
- `response.json()` est asynchrone et doit être attendu avec `await`.
- Une API est un intermédiaire entre React et la base de données.

### MySQL

- React ne doit pas contenir les identifiants MySQL.
- Les identifiants et secrets doivent être placés dans des variables d'environnement côté serveur.
- Utiliser des requêtes paramétrées pour éviter les injections SQL.
- Tester d'abord les routes API indépendamment de l'interface React.

## Difficultés enregistrées

_Aucune difficulté enregistrée pour le moment. Ajoute la première dès que tu bloques sur un exercice._
