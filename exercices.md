# Parcours d'exercices React — Fetch, API et MySQL

## Objectif général

Construire progressivement une application React qui communique avec une API REST, elle-même reliée à une base de données MySQL.

> Architecture cible : `React (frontend) → API FastAPI (backend Python) → MySQL (base de données)`
>
> React ne doit pas se connecter directement à MySQL. Le frontend appelle l'API, et l'API dialogue avec MySQL.

## Prérequis et outils

- JavaScript : variables, fonctions, tableaux, objets, `map`, `filter`, `async/await`
- React avec Vite
- Python 3, environnement virtuel et pip
- MySQL
- Un outil de test API : navigateur, Bruno, Postman ou Insomnia
- Git conseillé

---

## Niveau 1 — Bases React et données locales

### Exercice 1 — Afficher une liste de produits

Crée un composant `Produits` qui affiche une liste locale de cinq produits.

Chaque produit doit avoir un `id`, un `nom` et un `prix`.

**Compétences :** JSX, tableaux, `map`, props, clé `key`.

**Comment aborder :**

1. Crée le tableau de produits.
2. Affiche un titre.
3. Transforme chaque objet en élément JSX avec `map`.
4. Ajoute une `key` stable basée sur `id`.

**Fonctions et outils utiles :** `map()`, interpolation JSX, `key`.

### Exercice 2 — Filtrer les produits

Ajoute un champ de recherche. La liste affichée doit se limiter aux produits dont le nom contient le texte saisi, sans tenir compte des majuscules/minuscules.

**Compétences :** `useState`, événement `onChange`, input contrôlé, `filter`.

**Comment aborder :**

1. Crée un état pour le texte de recherche.
2. Relie l'input à cet état.
3. Crée une liste filtrée à partir de la liste originale.
4. Affiche un message si aucun produit ne correspond.

**Fonctions et outils utiles :** `useState()`, `toLowerCase()`, `includes()`, `filter()`.

---

## Niveau 2 — Premier fetch vers une API publique

### Exercice 3 — Charger des utilisateurs

Utilise une API publique de test comme `https://jsonplaceholder.typicode.com/users` pour afficher une liste d'utilisateurs.

Affiche au minimum le nom, l'e-mail et la ville.

**Compétences :** `fetch`, `useEffect`, `async/await`, état de chargement.

**Comment aborder :**

1. Prépare trois états : données, chargement et erreur.
2. Lance la requête dans `useEffect` au montage du composant.
3. Convertis la réponse avec `response.json()`.
4. Affiche un état différent selon chargement, erreur ou succès.

**Fonctions et outils utiles :** `fetch()`, `useEffect()`, `response.ok`, `response.json()`.

### Exercice 4 — Détails d'un utilisateur

Ajoute un bouton sur chaque utilisateur. Au clic, affiche ses informations détaillées dans un panneau ou une modale.

**Compétences :** état de sélection, événements, rendu conditionnel.

**Comment aborder :**

1. Stocke l'utilisateur sélectionné dans un état.
2. Passe l'utilisateur sélectionné au composant de détails.
3. Affiche le composant uniquement lorsqu'un utilisateur est sélectionné.
4. Ajoute un bouton pour fermer les détails.

**Fonctions et outils utiles :** `useState()`, rendu conditionnel avec `&&` ou ternaire.

---

## Niveau 3 — Créer un backend API

### Exercice 5 — Première API FastAPI

Crée un dossier `backend` séparé du frontend React. Initialise une API Python avec FastAPI et Uvicorn.

Crée les routes suivantes :

- `GET /api/health` → retourne `{ "message": "API opérationnelle" }`
- `GET /api/produits` → retourne une liste de produits en mémoire
- `GET /api/produits/{id}` → retourne un seul produit

**Compétences :** serveur HTTP, routes FastAPI, paramètres de chemin, JSON, documentation automatique.

**Comment aborder :**

1. Crée un environnement virtuel Python.
2. Installe `fastapi` et `uvicorn`.
3. Crée un fichier `main.py`.
4. Déclare les routes avec les décorateurs FastAPI.
5. Active le CORS pour autoriser React.
6. Lance le serveur avec Uvicorn.
7. Teste les routes dans `/docs` avant de connecter React.

**Fonctions et outils utiles :** `FastAPI()`, `@app.get()`, `Path`, `HTTPException`, `uvicorn`, `/docs`.

### Exercice 6 — Connecter React à ton API

Remplace l'API publique de l'exercice 3 par ton endpoint local `/api/produits`.

Ajoute une gestion correcte des erreurs lorsque le serveur backend est arrêté.

**Compétences :** communication frontend/backend, URL d'API, erreurs réseau, CORS.

**Comment aborder :**

1. Démarre le backend.
2. Vérifie l'endpoint directement dans le navigateur ou Bruno/Postman.
3. Remplace l'URL de `fetch` dans React.
4. Teste le cas normal puis le cas où l'API est indisponible.

**Fonctions et outils utiles :** `fetch()`, `try/catch`, `response.ok`, variables d'environnement Vite (`VITE_API_URL`).

---

## Niveau 4 — MySQL et opérations CRUD

### Exercice 7 — Créer la base de données

Crée une base MySQL nommée `catalogue` et une table `produits` avec les colonnes :

- `id` : identifiant auto-incrémenté
- `nom` : texte obligatoire
- `description` : texte
- `prix` : nombre décimal positif
- `stock` : entier positif
- `created_at` : date de création

Insère au moins cinq produits de test.

**Compétences :** SQL, table, contraintes, insertion.

**Comment aborder :**

1. Écris le script SQL de création.
2. Exécute-le dans MySQL.
3. Vérifie les lignes avec `SELECT * FROM produits`.
4. Teste les contraintes avec des valeurs invalides.

**Fonctions et outils utiles :** `CREATE DATABASE`, `CREATE TABLE`, `INSERT INTO`, `SELECT`.

### Exercice 8 — Relier FastAPI à MySQL

Dans le backend Python, utilise SQLAlchemy avec un driver MySQL pour créer une connexion ou un pool de connexions.

Modifie `GET /api/produits` afin de lire les produits depuis MySQL.

**Compétences :** variables d'environnement, SQLAlchemy, modèles, sessions de base de données, requêtes SQL côté serveur.

**Comment aborder :**

1. Installe `sqlalchemy`, un driver MySQL et `python-dotenv`.
2. Place les identifiants dans un fichier `.env` non versionné.
3. Crée un module de connexion et une session réutilisable.
4. Crée le modèle SQLAlchemy correspondant à `produits`.
5. Exécute la lecture dans la route FastAPI.
6. Ferme correctement chaque session.

**Fonctions et outils utiles :** `create_engine`, `sessionmaker`, `Session`, `Depends`, SQLAlchemy, requêtes paramétrées.

### Exercice 9 — CRUD complet

Ajoute les routes suivantes :

- `GET /api/produits/:id`
- `POST /api/produits`
- `PUT /api/produits/:id`
- `DELETE /api/produits/:id`

Valide les données reçues et retourne des codes HTTP cohérents.

**Compétences :** CRUD, validation, codes HTTP, sécurité SQL.

**Comment aborder :**

1. Vérifie les champs obligatoires avant la requête SQL.
2. Utilise uniquement des requêtes paramétrées.
3. Retourne `201` après création.
4. Retourne `404` si l'identifiant n'existe pas.
5. Retourne `400` si les données sont invalides.
6. Teste chaque route indépendamment.

**Fonctions et outils utiles :** `req.body`, `req.params`, `INSERT`, `UPDATE`, `DELETE`, codes HTTP.

---

## Niveau 5 — Application React complète

### Exercice 10 — Interface de gestion des produits

Construis une interface React qui permet de :

- charger les produits depuis l'API ;
- rechercher et filtrer les produits ;
- créer un produit avec un formulaire ;
- modifier un produit ;
- supprimer un produit avec confirmation ;
- afficher les états de chargement et d'erreur ;
- rafraîchir la liste après chaque modification.

**Compétences :** formulaires contrôlés, CRUD frontend, synchronisation avec l'API, composants.

**Comment aborder :**

1. Commence par l'affichage en lecture seule.
2. Ajoute le formulaire de création.
3. Ajoute la suppression.
4. Ajoute la modification.
5. Factorise les appels réseau dans un fichier `api.js`.
6. Sépare les composants : liste, formulaire, ligne produit, messages.

**Fonctions et outils utiles :** `useState`, `useEffect`, `fetch`, `POST`, `PUT`, `DELETE`, composants contrôlés.

### Exercice 11 — Pagination et recherche côté API

Ajoute une pagination et une recherche effectuée par le backend.

Exemple : `GET /api/produits?page=1&limit=10&search=clavier`.

**Compétences :** query parameters, pagination SQL, synchronisation URL/état.

**Comment aborder :**

1. Lis les paramètres avec `req.query`.
2. Valide `page` et `limit`.
3. Utilise `WHERE`, `LIKE`, `LIMIT` et `OFFSET` avec des paramètres sûrs.
4. Retourne les métadonnées : page courante, nombre total, nombre de pages.
5. Fais varier la requête React lorsque la page ou la recherche change.

**Fonctions et outils utiles :** `req.query`, `URLSearchParams`, `LIMIT`, `OFFSET`, `LIKE`.

### Exercice 12 — Authentification et projet final

Ajoute une authentification simple : inscription, connexion et route protégée pour modifier les produits.

Termine par une documentation du projet avec installation, variables d'environnement, scripts et routes API.

**Compétences :** authentification, mots de passe hachés, middleware, architecture complète.

**Comment aborder :**

1. Crée une table `users`.
2. Ne stocke jamais les mots de passe en clair.
3. Sépare les routes publiques et protégées.
4. Ajoute un middleware d'authentification.
5. Protège les opérations d'écriture.
6. Documente et teste toutes les routes.

**Fonctions et outils utiles :** dépendances FastAPI, middleware, hash de mot de passe, token, variables d'environnement, tests API.

---

## Méthode de travail pour chaque exercice

1. Lire uniquement l'objectif et les critères.
2. Écrire une première version sans chercher la solution complète.
3. Tester une fonctionnalité à la fois.
4. Noter chaque blocage dans `aide.md`.
5. Demander un indice avant une correction complète.
6. Vérifier le résultat dans le navigateur et/ou avec un outil API.
7. Ne passer à l'exercice suivant qu'après avoir compris la correction.
