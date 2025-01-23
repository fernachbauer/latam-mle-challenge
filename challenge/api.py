import os
import fastapi
from fastapi import HTTPException
import pandas as pd
from challenge.model import DelayModel
from pydantic import BaseModel, Field, validator
from typing import List
import traceback

app = fastapi.FastAPI()

# Inicializar el modelo
model = DelayModel()
MODEL_PATH = "challenge/xgboost_model.pkl"

if os.path.exists(MODEL_PATH):
    model.load_model(MODEL_PATH)
else:
    raise RuntimeError(f"Agrega un modelo entrenado en {MODEL_PATH}")

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {"status": "OK"}

# Definir el esquema esperado con nombres correctos sin FALLIDA
class FlightData(BaseModel):
    OPERA: str = Field(..., example="Aerolineas Argentinas")
    TIPOVUELO: str = Field(..., example="N")
    MES: int = Field(..., example=3, ge=1, le=12)
    Fecha_I: str = Field(..., alias="Fecha-I", example="2025-01-01 00:00:00")
    Fecha_O: str = Field(..., alias="Fecha-O", example="2025-01-01 02:00:00")
    SIGLAORI: str = Field(..., example="SCL")
    SIGLADES: str = Field(..., example="EZE")
    DIANOM: str = Field(..., example="Lunes")
    Vlo_I: str = Field(..., alias="Vlo-I", example="AR1234")
    Emp_I: str = Field(..., alias="Emp-I", example="AR")

    class Config:
        allow_population_by_field_name = True  # Permite usar alias en JSON

    @validator("TIPOVUELO")
    def check_tipo_vuelo(cls, value):
        if value not in ["N", "I"]:
            raise ValueError("TIPOVUELO debe ser 'N' (nacional) o 'I' (internacional)")
        return value

    @validator("Fecha_I", "Fecha_O")
    def validate_fecha_format(cls, value):
        valid_formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]
        for fmt in valid_formats:
            try:
                return pd.to_datetime(value, format=fmt).strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue
        raise ValueError("Formato de fecha inválido. Use '%Y-%m-%d %H:%M:%S' o '%Y-%m-%d'")

class PredictionRequest(BaseModel):
    flights: List[FlightData]

@app.post("/predict", status_code=200)
async def post_predict(request: PredictionRequest) -> dict:
    try:
        input_data = pd.DataFrame([flight.dict(by_alias=True) for flight in request.flights])

        # Lista de columnas esperadas
        required_columns = [
            "OPERA", "TIPOVUELO", "MES", "Fecha-I", "Fecha-O",
            "SIGLAORI", "SIGLADES", "DIANOM", "Vlo-I", "Emp-I"
        ]

        # Validar columnas faltantes
        missing_columns = [col for col in required_columns if col not in input_data.columns]
        if missing_columns:
            raise HTTPException(status_code=422, detail=f"Faltan columnas: {missing_columns}")

        # Verificar columnas desconocidas
        unknown_columns = [col for col in input_data.columns if col not in required_columns]
        if unknown_columns:
            raise HTTPException(status_code=422, detail=f"Columnas desconocidas: {unknown_columns}")

        # Procesamiento de datos
        processed_features = model.preprocess(input_data)
        predictions = model.predict(processed_features)

        return {"predict": predictions}

    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Error en la predicción: {str(e)}")
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"Error interno: {error_trace}")
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
