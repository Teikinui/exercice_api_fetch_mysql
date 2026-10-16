from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API React FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check():
    return {"message": "API opérationnelle"}


@app.get("/api/produits")
def get_produits():
    return [
        {"id": 1, "nom": "Clavier", "prix": 49.99},
        {"id": 2, "nom": "Souris", "prix": 24.99},
    ]
