import pandas as pd
import numpy as np
from datetime import datetime

# Columnas seleccionadas para el modelo
FEATURES_COLS = [
    "OPERA_Latin American Wings", 
    "MES_7",
    "MES_10",
    "OPERA_Grupo LATAM",
    "MES_12",
    "TIPOVUELO_I",
    "MES_4",
    "MES_11",
    "OPERA_Sky Airline",
    "OPERA_Copa Air"
]

# Nombre de la columna objetivo
TARGET_COL = "delay"

def get_period_day(date) -> str:
    """
    Determina el periodo del día en función de la hora de un vuelo.

    :param date: Fecha en formato string 'YYYY-MM-DD HH:MM:SS' o Timestamp.
    :return: Periodo del día ('mañana', 'tarde', 'noche')
    """
    try:
        # Convertir a cadena si es Timestamp
        if not isinstance(date, str):
            date = date.strftime('%Y-%m-%d %H:%M:%S')

        # Intentar parsear en el formato esperado
        date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').time()

        morning_min = datetime.strptime("05:00", '%H:%M').time()
        morning_max = datetime.strptime("11:59", '%H:%M').time()
        afternoon_min = datetime.strptime("12:00", '%H:%M').time()
        afternoon_max = datetime.strptime("18:59", '%H:%M').time()

        if morning_min <= date_time <= morning_max:
            return 'mañana'
        elif afternoon_min <= date_time <= afternoon_max:
            return 'tarde'
        else:
            return 'noche'
    except ValueError as ve:
        raise ValueError(f"Error en get_period_day: formato de fecha inválido ({date}). Use 'YYYY-MM-DD HH:MM:SS'. Error: {ve}")
    except Exception as e:
        raise ValueError(f"Error en get_period_day: {e}")

def is_high_season(fecha: str) -> int:
    """
    Determina si una fecha pertenece a la temporada alta.

    :param fecha: Fecha en formato string 'YYYY-MM-DD HH:MM:SS'
    :return: 1 si es temporada alta, 0 en caso contrario.
    """
    try:
        fecha_año = int(fecha.split('-')[0])
        fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')

        # Rangos de temporada alta
        ranges = [
            ('15-Dec', '31-Dec'),
            ('1-Jan', '3-Mar'),
            ('15-Jul', '31-Jul'),
            ('11-Sep', '30-Sep')
        ]
        
        for start, end in ranges:
            if datetime.strptime(start, '%d-%b').replace(year=fecha_año) <= fecha <= datetime.strptime(end, '%d-%b').replace(year=fecha_año):
                return 1
        return 0
    except Exception as e:
        raise ValueError(f"Error en is_high_season: {e}")

def get_min_diff(row) -> float:
    """
    Calcula la diferencia de minutos entre Fecha-I y Fecha-O.

    :param row: Fila del DataFrame con las fechas de entrada y salida.
    :return: Diferencia en minutos.
    """
    try:
        fecha_o = datetime.strptime(row['Fecha-O'], '%Y-%m-%d %H:%M:%S')
        fecha_i = datetime.strptime(row['Fecha-I'], '%Y-%m-%d %H:%M:%S')
        return (fecha_o - fecha_i).total_seconds() / 60
    except Exception as e:
        raise ValueError(f"Error en get_min_diff: {e}")

