from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.coingecko import get_project
from app.analyzer import build_prompt, analyze_project

app = FastAPI(title="Crypto Analyzer Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze/{coin_id}")
def analyze(coin_id: str):
    data = get_project(coin_id)
    if not data:
        raise HTTPException(status_code=404, detail="Progetto non trovato")

    prompt = build_prompt(data)
    analysis = analyze_project(prompt)

    return {
        "project": data["name"],
        "analysis": analysis,
        "disclaimer": "Questo contenuto non è un consiglio finanziario"
    }
