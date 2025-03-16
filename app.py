from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pickle
import pandas as pd
from lightgbm import LGBMClassifier
import numpy as np

# Initialisierung der API
app = FastAPI()

# Laden des trainierten Modells 
with open('lgbm_model.pkl', "rb") as file:
    model = pickle.load(file)

# Eingabedaten definieren
class InputData(BaseModel):
    Produktname: str
    Reisedauer: float
    Reiseziel: str
    Nettoumsatz: float
    Kommission: float
    Alter: float

# 4Ausgabeformat definieren
class PredictionResponse(BaseModel):
    Leistungswahrscheinlichkeit: float

# API-Endpunkt für Vorhersagen
@app.post("/predict", response_model=PredictionResponse)
async def predict(data: InputData):
    # Eingabedaten in ein DataFrame umwandeln
    df = pd.DataFrame([data.dict()])
    df = df[['Produktname', 'Reisedauer', 'Reiseziel', 'Nettoumsatz', 'Kommission', 'Alter']]
    df = df.astype({'Produktname': 'category', 'Reiseziel': 'category'})

    # Falls Preprocessing notwendig ist, hier hinzufügen (z. B. Encoding)
    # df = preprocess(df)

    # Modellvorhersage
    prediction_proba = model.predict_proba(df)[:, 1][0]
    
    return {"Leistungswahrscheinlichkeit": round(prediction_proba, 4)}
