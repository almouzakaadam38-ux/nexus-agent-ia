from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Ce code dit au Cloud d'afficher ton interface visuelle
    if os.path.exists("nexus_agent_dashboard.html"):
        with open("nexus_agent_dashboard.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Erreur : Fichier interface non trouvé sur le Cloud</h1>"
    
