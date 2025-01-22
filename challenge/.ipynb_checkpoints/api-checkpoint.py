import fastapi
from fastapi import HTTPException
from pydantic import BaseModel
import pandas as pd
from typing import List
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
    Entrena el modelo con los datos disponibles.
    """
    try:
        data = model.load_data("data/data.csv")
        features, target = model.preprocess(data, target_column="delay")
        report = model.fit(features, target)
        return {"message": "Modelo entrenado con éxito", "report": report}
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

        # Realizar predicciones
        predictions = model.predict(features)

        return PredictionResponse(predictions=predictions)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error de predicción: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
