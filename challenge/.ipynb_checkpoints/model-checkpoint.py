import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from typing import List, Tuple
from challenge.preprocessing import get_period_day, is_high_season, get_min_diff, FEATURES_COLS, TARGET_COL

class DelayModel:
    def __init__(self, random_state: int = 1, learning_rate: float = 0.01):
        """
        Inicializa el modelo XGBoost con hiperparámetros predefinidos.
        """
        self.random_state = random_state
        self.learning_rate = learning_rate
        self.scale_pos_weight = None
        self._model = None
        self.is_trained = False  # Flag to check if model is trained

    def load_data(self, filepath: str) -> pd.DataFrame:
        """
        Carga los datos desde un archivo CSV.

        :param filepath: Ruta del archivo CSV.
        :return: DataFrame con los datos cargados.
        """
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise FileNotFoundError(f"Error al cargar el archivo {filepath}: {e}")

    def preprocess(self, data: pd.DataFrame, target_column: str = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Preprocesa los datos utilizando funciones auxiliares.

        :param data: DataFrame con los datos crudos.
        :param target_column: Nombre de la columna objetivo, si se proporciona.
        :return: Tupla con los datos preprocesados (X, y) si se proporciona la columna objetivo, solo X en caso contrario.
        """
        try:
            # Generación de nuevas características
            data['period_day'] = data['Fecha-I'].apply(get_period_day)
            data['high_season'] = data['Fecha-I'].apply(is_high_season)
            data['min_diff'] = data.apply(get_min_diff, axis=1)

            # Definición de la variable objetivo 'delay'
            threshold_in_minutes = 15
            data['delay'] = np.where(data['min_diff'] > threshold_in_minutes, 1, 0)


            # One-hot encoding de variables categóricas
            encoded_data = pd.get_dummies(data, columns=['OPERA', 'MES', 'TIPOVUELO'], drop_first=True)

            # Asegurar que todas las columnas esperadas están presentes
            for col in FEATURES_COLS:
                if col not in encoded_data.columns:
                    encoded_data[col] = 0

            # Guardar el dataset procesado
            encoded_data.to_csv("data/data_processed.csv", index=False)

            feature_data = encoded_data[FEATURES_COLS]

            if target_column:
                target_data = pd.DataFrame(data[target_column], columns=[target_column])
                return feature_data, target_data

            return feature_data

        except Exception as e:
            raise ValueError(f"Error en preprocess: {e}")

    def fit(self, features: pd.DataFrame, target: pd.DataFrame, test_size: float = 0.33):
        """
        Divide los datos en entrenamiento y prueba, y entrena el modelo.

        :param features: DataFrame con las características.
        :param target: DataFrame con la variable objetivo.
        :param test_size: Tamaño de la partición de prueba.
        :return: Reporte de evaluación del modelo.
        """
        try:
            # División de datos en conjunto de entrenamiento y prueba
            x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=test_size, random_state=42)

            # Calcular el balance de clases
            n_y0 = len(y_train[y_train['delay'] == 0])
            n_y1 = len(y_train[y_train['delay'] == 1])
            self.scale_pos_weight = n_y0 / n_y1

            # Entrenamiento del modelo
            self._model = xgb.XGBClassifier(
                random_state=self.random_state,
                learning_rate=self.learning_rate,
                scale_pos_weight=self.scale_pos_weight
            )
            self._model.fit(x_train, y_train)

            self.is_trained = True  # Model is trained

            # Evaluación del modelo
            report = classification_report(y_test, self._model.predict(x_test), output_dict=True)
            return report

        except Exception as e:
            raise ValueError(f"Error en fit: {e}")

    def predict(self, features: pd.DataFrame) -> List[int]:
        """
        Realiza predicciones con el modelo entrenado.

        :param features: DataFrame con las características para realizar la predicción.
        :return: Lista de predicciones.
        """
        if not self.is_trained:
            raise ValueError("El modelo no ha sido entrenado aún.")
        
        try:
            return self._model.predict(features).tolist()
        except Exception as e:
            raise ValueError(f"Error en predict: {e}")
