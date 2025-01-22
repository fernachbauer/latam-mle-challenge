import os
import pandas as pd
from challenge.model import DelayModel

# Definir rutas
DATA_PATH = "data/data.csv"
MODEL_PATH = "challenge/xgboost_model.pkl"

def train_model():
    try:
        # Inicializar el modelo
        model = DelayModel()

        # Cargar los datos
        print("Cargando datos...")
        data = model.load_data(DATA_PATH)

        # Preprocesar los datos
        print("Preprocesando datos...")
        features, target = model.preprocess(data, target_column="delay")

        # Entrenar el modelo
        print("Entrenando modelo...")
        report = model.fit(features, target)

        # Guardar el modelo entrenado
        print(f"Guardando modelo en {MODEL_PATH}...")
        model.save_model(MODEL_PATH)

        print("Modelo entrenado y guardado exitosamente.")
        print("Reporte de evaluación:")
        print(report)

    except Exception as e:
        print(f"Error durante el entrenamiento: {e}")

if __name__ == "__main__":

    
    train_model()
