import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
# 1. On récupère le dossier où se trouve actuellement main.py (le dossier 'api')
dossier_actuel = os.path.dirname(os.path.abspath(__file__))

# 2. On remonte d'un cran ("..") pour pointer vers le dossier parent, puis on cible le fichier
chemin_modele = os.path.join( "..", "model", "model.pkl")

# Chargement du modèle (il faut que le fichier existe)
model = joblib.load(chemin_modele)

# Structure des données entrantes
class Data(BaseModel):
    features: list[float]

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(input_data: Data):
    # Transformation et prédiction
    prediction = model.predict([input_data.features])
    return {"prediction": prediction.tolist()}