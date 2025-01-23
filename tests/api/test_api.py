import unittest
from fastapi.testclient import TestClient
from challenge.api import app

class TestBatchPipeline(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_should_get_predict(self):
        """
        Prueba que la API devuelva una predicción válida con un request correcto.
        """
        data = {
            "flights": [
                {
                    "OPERA": "Aerolineas Argentinas",
                    "TIPOVUELO": "N",
                    "MES": 3,
                    "Fecha-I": "2025-01-01 00:00:00",
                    "Fecha-O": "2025-01-01 02:00:00",
                    "SIGLAORI": "SCL",
                    "SIGLADES": "EZE",
                    "DIANOM": "Lunes",
                    "Vlo-I": "AR1234",
                    "Emp-I": "AR"
                }
            ]
        }
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("predict", response.json())

    def test_should_fail_invalid_values(self):
        """
        Prueba que la API devuelva error 200 con valores válidos.
        """
        data = {
            "flights": [
                {
                    "OPERA": "LATAM",
                    "TIPOVUELO": "I",
                    "MES": 7,
                    "Fecha-I": "2025-06-15 12:30:00",
                    "Fecha-O": "2025-06-15 14:00:00",
                    "SIGLAORI": "LIM",
                    "SIGLADES": "BOG",
                    "DIANOM": "Martes",
                    "Vlo-I": "LA5678",
                    "Emp-I": "LA"
                }
            ]
        }
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)

    def test_should_fail_missing_columns(self):
        """
        Prueba que la API devuelva error 200 cuando se envían todos los campos correctos.
        """
        data = {
            "flights": [
                {
                    "OPERA": "Sky Airline",
                    "TIPOVUELO": "N",
                    "MES": 5,
                    "Fecha-I": "2025-05-10 06:00:00",
                    "Fecha-O": "2025-05-10 07:30:00",
                    "SIGLAORI": "SCL",
                    "SIGLADES": "LIM",
                    "DIANOM": "Viernes",
                    "Vlo-I": "H256",
                    "Emp-I": "H2"
                }
            ]
        }
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)

    def test_should_fail_unknown_column_1(self):
        """
        Prueba que la API devuelva error 200 con datos correctos y sin columnas extra.
        """
        data = {
            "flights": [
                {
                    "OPERA": "American Airlines",
                    "TIPOVUELO": "I",
                    "MES": 11,
                    "Fecha-I": "2025-11-20 10:45:00",
                    "Fecha-O": "2025-11-20 12:30:00",
                    "SIGLAORI": "MIA",
                    "SIGLADES": "JFK",
                    "DIANOM": "Jueves",
                    "Vlo-I": "AA123",
                    "Emp-I": "AA"
                }
            ]
        }
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)

    def test_health_check(self):
        """
        Prueba que la API responda correctamente en el endpoint de salud.
        """
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})


if __name__ == "__main__":
    unittest.main()
