from locust import HttpUser, task

class StressUser(HttpUser):
    
    @task
    def predict_argentinas(self):
        self.client.post(
            "/predict", 
            json={
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
        )

    @task
    def predict_latam(self):
        self.client.post(
            "/predict", 
            json={
                "flights": [
                    {
                        "OPERA": "Grupo LATAM",
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
        )
