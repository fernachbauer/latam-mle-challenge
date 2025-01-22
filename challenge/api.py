import os
import fastapi
from fastapi import HTTPException
import pandas as pd
from challenge.model import DelayModel
from pydantic import BaseModel
from typing import List

app = fastapi.FastAPI()

# Inicializar el modelo
model = DelayModel()
MODEL_PATH = "challenge/xgboost_model.pkl"

# Cargar el modelo si existe
if os.path.exists(MODEL_PATH):
    model.load_model(MODEL_PATH)
else:
    raise RuntimeError(f"Agrega un modelo entrenado en {MODEL_PATH}")


@app.get("/health", status_code=200)
async def get_health() -> dict:
    """
    Endpoint para verificar el estado de la API.
    """
    return {"status": "OK"}


class PredictionRequest(BaseModel):
    data: List[dict]


@app.post("/predict", status_code=200)
async def post_predict(request: PredictionRequest) -> dict:
    """
    Endpoint para realizar predicciones sobre los datos proporcionados.
    """
    try:
        # Convertir datos de entrada en un DataFrame de pandas
        input_data = pd.DataFrame(request.data)

        # Preprocesamiento de datos
        processed_features = model.preprocess(input_data)

        # Realizar predicción con el modelo
        predictions = model.predict(processed_features)

        return {"predictions": predictions}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en la predicción: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
