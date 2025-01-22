import fastapi
from fastapi import HTTPException
from pydantic import BaseModel
import pandas as pd
from typing import List
import joblib
import os
from challenge.model import DelayModel

# Inicializar la aplicación FastAPI
app = fastapi.FastAPI()

# Instanciar el modelo
model = DelayModel()

# Definir esquema de entrada para predicción
class PredictionInput(BaseModel):
    data: List[dict]

# Definir esquema de salida para predicción
class PredictionResponse(BaseModel):
    predictions: List[int]

@app.get("/health", status_code=200)
async def get_health() -> dict:
    """
    Endpoint para verificar el estado de la API.
    """
    return {"status": "OK"}

@app.post("/train", status_code=200)
async def post_train() -> dict:
    """
    Entrena el modelo con los datos disponibles y guarda el modelo en Google Cloud Storage.
    """
    try:
        # Cargar y preprocesar los datos
        data = model.load_data("data/data.csv")
        features, target = model.preprocess(data, target_column="delay")

        # Entrenar el modelo
        report = model.fit(features, target)

        # Guardar el modelo entrenado localmente
        joblib.dump(model._model, "model.pkl")

        # Subir a GCS si está configurado
        if "GCS_BUCKET" in os.environ:
            from google.cloud import storage
            client = storage.Client()
            bucket = client.bucket(os.environ["GCS_BUCKET"])
            blob = bucket.blob("model.pkl")
            blob.upload_from_filename("model.pkl")

        return {"message": "Modelo entrenado y guardado exitosamente", "report": report}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en entrenamiento: {str(e)}")

@app.post("/predict", status_code=200, response_model=PredictionResponse)
async def post_predict(input_data: PredictionInput) -> PredictionResponse:
    """
    Realiza predicciones basadas en los datos de entrada proporcionados.
    """
    try:
        # Convertir datos de entrada a DataFrame
        df = pd.DataFrame(input_data.data)

        # Preprocesamiento para predicción
        features = model.preprocess(df)

        # Verificar si el modelo está disponible, cargar desde GCS si es necesario
        if model._model is None and os.path.exists("model.pkl"):
            model._model = joblib.load("model.pkl")
        elif model._model is None and "GCS_BUCKET" in os.environ:
            from google.cloud import storage
            client = storage.Client()
            bucket = client.bucket(os.environ["GCS_BUCKET"])
            blob = bucket.blob("model.pkl")
            blob.download_to_filename("model.pkl")
            model._model = joblib.load("model.pkl")

        # Realizar predicciones
        predictions = model.predict(features)

        return PredictionResponse(predictions=predictions)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error de predicción: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
