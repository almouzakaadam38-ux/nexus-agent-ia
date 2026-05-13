from fastapi import FastAPI
import os

app = FastAPI()

# Configuration de tes paiements (Mobile et Carte Visa)
PAYMENT_METHODS = "Moov: +235 93643188 | Airtel: +235 64107740 | Visa: 4646 6384 1124 8965"
FREE_LIMIT = 4

user_usage = {}

@app.get("/")
def home():
    return {"message": "Nexus Agent IA - Global Content Strategy", "status": "Online"}

@app.get("/search")
def search(user_id: str, query: str):
    count = user_usage.get(user_id, 0)
    
    if count >= FREE_LIMIT:
        return {
            "blocked": True,
            "message": f"🔒 Limite gratuite atteinte ({FREE_LIMIT} recherches).",
            "instruction": "Pour débloquer l'accès illimité, envoyez votre paiement via Moov, Airtel ou Carte Visa :",
            "contacts": PAYMENT_METHODS
        }
    
    user_usage[user_id] = count + 1
    
    return {
        "blocked": False,
        "results": f"Analyse stratégique pour : '{query}'",
        "remaining_free": FREE_LIMIT - (count + 1)
    }
