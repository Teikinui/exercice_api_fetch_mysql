# Projet React + FastAPI + MySQL

Application pédagogique construite progressivement avec :

- **React + Vite** pour le frontend ;
- **FastAPI** pour l'API REST en Python ;
- **MySQL** pour la base de données ;
- **Docker Compose** pour lancer les services ;
- **SQLAlchemy** pour communiquer avec MySQL.

## Architecture

```text
Navigateur
    │
    ▼
React + Vite ─── fetch ───► FastAPI ─── SQLAlchemy ───► MySQL
```

React ne se connecte jamais directement à MySQL. Les identifiants de base de données restent dans le backend.

## Structure prévue

```text
.
├── frontend/              # Application React + Vite
├── backend/               # API FastAPI
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── exercices.md           # Parcours pédagogique
├── aide.md                # Difficultés et rappels
├── docker-compose.yml     # Services API et MySQL
├── .env.example           # Exemple de configuration
├── .gitignore
└── README.md
```

## Prérequis

Installer :

- Docker Desktop ou Docker Engine avec le plugin Compose ;
- Git ;
- Node.js et npm si le frontend est lancé en dehors de Docker ;
- Python 3 et `pip` si le backend est lancé en dehors de Docker ;
- un outil de test API comme Bruno, Postman ou Insomnia.

Vérifier l'installation :

```bash
docker --version
docker compose version
node --version
python --version
```

## Installation

Cloner le projet puis entrer dans son dossier :

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_PROJET>
```

Créer le fichier de configuration local à partir de l'exemple :

```bash
cp .env.example .env
```

Ne jamais commit le fichier `.env`. Il peut contenir des mots de passe.

## Variables d'environnement

Exemple de configuration à adapter dans `.env` :

```env
MYSQL_DATABASE=catalogue
MYSQL_USER=app_user
MYSQL_PASSWORD=change-moi
MYSQL_ROOT_PASSWORD=change-moi-aussi
MYSQL_HOST=mysql
MYSQL_PORT=3306

DATABASE_URL=mysql+pymysql://app_user:change-moi@mysql:3306/catalogue

API_PORT=8000
VITE_API_URL=http://localhost:8000
```

Dans Docker, le serveur FastAPI utilise `mysql` comme nom d'hôte car il s'agit du nom du service Docker. Depuis le navigateur, React utilise `localhost` et le port exposé par Docker.

## Démarrage avec Docker Compose

Construire les images et démarrer les services :

```bash
docker compose up --build
```

Démarrer en arrière-plan :

```bash
docker compose up --build -d
```

Adresses utiles :

- API : `http://localhost:8000`
- Documentation interactive FastAPI : `http://localhost:8000/docs`
- Documentation alternative : `http://localhost:8000/redoc`
- MySQL : `localhost:3306`, si le port est exposé

Afficher les logs :

```bash
docker compose logs -f api
docker compose logs -f mysql
```

Arrêter les conteneurs sans supprimer les données :

```bash
docker compose down
```

Arrêter les conteneurs et supprimer aussi le volume MySQL :

```bash
docker compose down -v
```

> La commande `down -v` supprime les données de la base. À utiliser uniquement lorsque cela est voulu.

## Lancer le frontend

Depuis le dossier `frontend` :

```bash
npm install
npm run dev
```

Le frontend sera généralement accessible sur `http://localhost:5173`.

L'URL de l'API doit être configurée dans `frontend/.env` :

```env
VITE_API_URL=http://localhost:8000
```

Exemple d'appel depuis React :

```js
const response = await fetch(`${import.meta.env.VITE_API_URL}/api/produits`);

if (!response.ok) {
  throw new Error("Erreur lors du chargement des produits");
}

const produits = await response.json();
```

## Lancer le backend sans Docker

Cette méthode est utile pour le développement et le débogage du code Python.

Depuis le dossier `backend` :

```bash
python -m venv .venv
```

Activation sous Linux ou WSL :

```bash
source .venv/bin/activate
```

Activation sous Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer FastAPI :

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Dans ce cas, MySQL peut continuer à fonctionner dans Docker. Depuis le backend lancé directement sur la machine, l'hôte MySQL peut devoir être `127.0.0.1` au lieu de `mysql`, selon la configuration utilisée.

## Tests de l'API

Tester l'état de l'API :

```bash
curl http://localhost:8000/api/health
```

Tester la liste des produits :

```bash
curl http://localhost:8000/api/produits
```

Les routes peuvent aussi être testées depuis la documentation interactive :

```text
http://localhost:8000/docs
```

## Qualité et tests

Backend :

```bash
ruff check backend
pytest backend/tests
```

Frontend :

```bash
cd frontend
npm run build
npm run test
```

Les commandes exactes pourront être adaptées lorsque les fichiers de configuration du frontend et du backend seront créés.

## Développement recommandé

1. Commencer par l'exercice 0 dans `exercices.md`.
2. Vérifier que Docker Compose démarre correctement.
3. Tester l'API FastAPI dans `/docs`.
4. Créer la base et vérifier MySQL.
5. Connecter React avec `fetch`.
6. Ajouter les opérations CRUD progressivement.
7. Noter chaque difficulté dans `aide.md`.
8. Tester après chaque modification.

## Règles importantes

- Ne jamais mettre les identifiants MySQL dans React.
- Ne jamais commiter `.env`.
- Utiliser des requêtes paramétrées ou SQLAlchemy.
- Vérifier les données reçues par l'API avec des modèles Pydantic.
- Gérer les états de chargement, succès et erreur dans React.
- Ne pas supprimer le volume MySQL sans vérifier que les données peuvent être perdues.
