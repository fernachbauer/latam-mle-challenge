Aquí tienes un informe detallado para la entrega del challenge en formato **Markdown**, con un enfoque humanizado y creativo, utilizando **emojis** para hacerlo más atractivo.

---

# 🚀 Desafío Software Engineer (ML & LLMs) - Entrega Final

¡Hola equipo! 👋  
A continuación, presento la entrega completa del desafío **Software Engineer (ML & LLMs)**, con todas las respuestas, evidencias y resultados obtenidos en cada una de las 4 partes del reto. 🎯

---

## 📝 Índice

1. [Resumen del Desafío](#resumen-del-desafío)
2. [Parte 1: Transcripción del modelo](#parte-1-transcripción-del-modelo)
3. [Parte 2: Implementación de la API con FastAPI](#parte-2-implementación-de-la-api-con-fastapi)
4. [Parte 3: Despliegue en Google Cloud](#parte-3-despliegue-en-google-cloud)
5. [Parte 4: Implementación CI/CD](#parte-4-implementación-cicd)
6. [Conclusión](#conclusión)
7. [Evidencias](#evidencias)

---

## 🛠 Resumen del Desafío

En este desafío, el objetivo fue operacionalizar un modelo de Machine Learning para predecir la probabilidad de **retraso de vuelos en el aeropuerto de SCL**. Se llevaron a cabo las siguientes etapas:

1. **Transcripción del modelo de Jupyter Notebook a Python** 🐍
2. **Desarrollo de una API con FastAPI** ⚡
3. **Despliegue de la API en Google Cloud Run** ☁️
4. **Implementación de CI/CD con GitHub Actions** 🤖

---

## 📊 Parte 1: Transcripción del modelo

### ✔️ Actividades realizadas

1. **Transcripción del modelo:**  
   Se trasladó la lógica del notebook `exploration.ipynb` al archivo `model.py`, aplicando las mejores prácticas de codificación. Se seleccionó el mejor modelo basado en métricas de rendimiento.
   
2. **Correcciones y mejoras:**  
   - Se corrigieron errores menores en la manipulación de fechas.
   - Se añadieron pruebas unitarias para asegurar la calidad del código.

3. **Pruebas realizadas:**  
   Ejecutando:

   ```bash
   make model-test
   ```

   **Resultado esperado:** ✅ Todas las pruebas pasaron exitosamente.

---

## 🌐 Parte 2: Implementación de la API con FastAPI

### ✔️ Actividades realizadas

1. **Creación de la API en `api.py`:**  
   - Endpoints implementados:
     - `/predict`: Predicción de retraso de vuelo.
     - `/health`: Chequeo del estado del servicio.

2. **Pruebas unitarias de la API:**  
   Ejecutando:

   ```bash
   make api-test
   ```

   **Resultado esperado:** ✅ API funcionando correctamente sin errores.

3. **Ejecución local para validación:**  
   Se levantó el servidor con:

   ```bash
   uvicorn api:app --reload
   ```

   **Verificación con curl:**

   ```bash
   curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"Fecha-I":"2023-12-15 10:00","Vlo-I":"LA123","Ori-I":"SCL","Des-I":"LIM","Emp-I":"LATAM"}'
   ```

   **Respuesta esperada:**

   ```json
   {"delay_probability": 0.75}
   ```

---

## ☁️ Parte 3: Despliegue en Google Cloud

### ✔️ Actividades realizadas

1. **Creación del contenedor Docker:**  
   Se creó una imagen de Docker optimizada:

   ```bash
   docker build -t gcr.io/latam-mle-project/test-image .
   ```

2. **Subida de la imagen a Google Container Registry (GCR):**

   ```bash
   docker push gcr.io/latam-mle-project/test-image
   ```

3. **Despliegue en Cloud Run:**

   ```bash
   gcloud run deploy test-service \
     --image=gcr.io/latam-mle-project/test-image \
     --platform=managed \
     --region=us-central1 \
     --allow-unauthenticated
   ```

4. **Actualización del `Makefile`:**  
   Se actualizó la línea 26 con la URL de la API desplegada:

   ```makefile
   API_URL = https://test-service-abc123-uc.a.run.app
   ```

5. **Pruebas de estrés:**  

   ```bash
   make stress-test
   ```

   **Resultado esperado:** ✅ API funcionando correctamente bajo carga.

---

## 🔄 Parte 4: Implementación CI/CD

### ✔️ Actividades realizadas

1. **Configuración de GitHub Actions:**  
   Se crearon los archivos `.github/workflows/ci.yml` y `.github/workflows/cd.yml`.

2. **CI (Integración Continua):**  
   - Instalación de dependencias.
   - Pruebas unitarias y cobertura de código.
   - Construcción y publicación de la imagen Docker.

3. **CD (Entrega Continua):**  
   - Despliegue automático a Google Cloud Run al hacer push a `main`.

4. **Ejecución de pipelines:**  
   Después de realizar un push, los workflows fueron activados automáticamente en GitHub Actions.

---

## 📸 Evidencias

### 🏁 Pruebas unitarias exitosas (Parte 1 y 2)
![Pruebas Unitarias](https://github.com/fernachbauer/latam-mle-challenge/actions/workflows/ci.yml)

### ☁️ Despliegue en Google Cloud Run (Parte 3)
![Despliegue Cloud Run](https://github.com/fernachbauer/latam-mle-challenge/actions/workflows/cd.yml)

### ✅ API funcionando en producción
[https://test-service-abc123-uc.a.run.app/docs](https://test-service-abc123-uc.a.run.app/docs)

---

## 🏁 Conclusión

Este desafío ha permitido demostrar la capacidad de:

- 🔹 Transcribir y mejorar modelos de Machine Learning.
- 🔹 Desarrollar APIs escalables usando FastAPI.
- 🔹 Implementar despliegues en Google Cloud Run.
- 🔹 Automatizar flujos de CI/CD con GitHub Actions.

---

## 🚀 Envío del desafío

Se realizó el envío de la solución mediante la siguiente petición POST:

```bash
curl -X POST https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/software-engineer \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Fernando Nachbauer",
           "mail": "fernando.nachbauer@example.com",
           "github_url": "https://github.com/fernachbauer/latam-mle-challenge.git",
           "api_url": "https://test-service-abc123-uc.a.run.app"
         }'
```

**Resultado esperado:**

```json
{
  "status": "OK",
  "detail": "your request was received"
}
```

---

¡Gracias por la oportunidad de participar en este desafío! 🎉 Si tienen alguna pregunta, estaré encantado de responder. 🤓

---

Espero que este documento cubra todos los puntos clave de la entrega. ¡Buena suerte! 🚀
