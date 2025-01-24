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
## 🛠 Tecnologías Utilizadas

El desarrollo del proyecto se basó en diversas tecnologías para garantizar su correcto funcionamiento:

- **Lenguajes de programación:**
  - Python 3.11
  - Jupyter Notebooks

- **Frameworks y librerías:**
  - FastAPI (para la construcción de la API)
  - Pytest (para las pruebas unitarias y de integración)
  - Locust (para pruebas de carga)
  - Pandas, NumPy, Scikit-learn, XGBoost (para procesamiento y entrenamiento del modelo)

- **Herramientas de DevOps y CI/CD:**
  - GitHub Actions (para integración y despliegue continuo)
  - Docker (contenedorización de la aplicación)
  - Google Cloud Platform (GCP):
    - Cloud Run (despliegue de la API)
    - Cloud Storage (almacenamiento de artefactos del modelo)
    - Artifact Registry (almacenamiento de imágenes de Docker)

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

   **Resultados:**

   ✅ Todas las pruebas pasaron exitosamente.

**Preprocesamiento de los datos:** 
    - Se ajustaron los datos de entrada para cumplir con los requisitos del modelo.
    - Problemas encontrados: errores en la limpieza de datos y formatos incorrectos de fechas.

**Entrenamiento del modelo:** 
    - Se probaron varios modelos, seleccionando finalmente **XGBoost**, ya que presentó el mejor balance entre precisión y sensibilidad en la predicción de atrasos.

**Evaluación del modelo:** 
    - La métrica más relevante para el negocio se definió como **recall**, para minimizar los falsos negativos.

**Principales dificultades:**
- Problemas de sintaxis en los gráficos de Jupyter Notebooks que se corrigieron manualmente.
- Ajuste de hiperparámetros para mejorar la precisión sin comprometer el rendimiento.

---

## 🌐 Parte 2: Implementación de la API con FastAPI

### ✔️ Actividades realizadas


### Construcción de la API con FastAPI**

Se implementó una API REST utilizando FastAPI que incluye los siguientes endpoints:

| Método  | Endpoint    | Descripción                                |
|---------|-------------|--------------------------------------------|
| `GET`   | `/health`    | Verifica el estado de la API               |
| `POST`  | `/predict`   | Recibe datos de vuelos y devuelve predicciones |

**Formato de solicitud esperado:**
```json
{
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
```

1. **Creación de la API en `api.py`:**  
   - Endpoints implementados:
     - `/predict`: Predicción de retraso de vuelo.
     - `/health`: Chequeo del estado del servicio.
![image](https://github.com/user-attachments/assets/2837a1f0-2001-4361-b589-41d4ab8da76b)

2. **Pruebas unitarias de la API:**  
   Ejecutando:

   ```bash
   make api-test
   ```
![image](https://github.com/user-attachments/assets/f75d410e-4526-48c8-8870-b04ca1049ab3)


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
# **Principales dificultades:**

Ajuste de dependencias en requirements.txt debido a incompatibilidades con versiones de Python.
Faltaban validaciones en los datos de entrada, lo que generaba errores de API.
Se tuvo que completar las pruebas de validación para cubrir todas las casuísticas posibles.

---

## ☁️ Parte 3: Despliegue en Google Cloud

### ✔️ Actividades realizadas

Se realizaron pruebas de carga utilizando Locust para validar la escalabilidad de la API con 100 usuarios concurrentes. Los resultados mostraron:

Peticiones exitosas: 100%
Tiempo de respuesta promedio: 1128 ms
Máximo tiempo de respuesta: 9342 ms
Usuarios concurrentes: 100

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
   API_URL = https://latam-api-700756977721.us-central1.run.app
   ```

5. **Pruebas de estrés:**  

   ```bash
   make stress-test
   ```
   
# **Principales dificultades:**

Configuración de variables de entorno para la ejecución de las pruebas.
Identificación de latencias inesperadas debido a la carga del servidor.

   **Resultado esperado:** ✅ API funcionando correctamente bajo carga.
   
![image](https://github.com/user-attachments/assets/32dca277-4493-4dcc-bcaf-69c32b9010af)

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

### 🏁 Pruebas unitarias incorporadas al flujo (Parte 1 y 2)
![Pruebas Unitarias](https://github.com/fernachbauer/latam-mle-challenge/actions/workflows/ci.yml)

### ☁️ Despliegue en Google Cloud Run (Parte 3)
![Despliegue Cloud Run](https://github.com/fernachbauer/latam-mle-challenge/actions/workflows/cd.yml)

### ✅ API funcionando en producción
https://latam-api-700756977721.us-central1.run.

## **Principales desafíos:**

Configuración de permisos para la cuenta de servicio.
Problemas con la subida de imágenes a Google Artifact Registry.
Se tuvo que mejorar la configuración de memoria y CPU en Cloud Run para manejar la carga de trabajo esperada.

## Consumo de la API del Modelo

Para interactuar con la API del modelo de predicción, puedes utilizar la herramienta `curl` para enviar solicitudes HTTP. A continuación, se proporciona un ejemplo de cómo realizar una consulta `POST` a la API para obtener una predicción.

### Endpoint de la API

La API está desplegada en la siguiente URL:

https://latam-api-700756977721.us-central1.run.app

### Formato de la solicitud

Se debe realizar una solicitud `POST` al endpoint `/predict` con los datos de vuelo en formato JSON. La estructura del JSON debe incluir las siguientes columnas requeridas:

| Campo    | Tipo  | Descripción                          | Ejemplo                   |
|----------|-------|--------------------------------------|---------------------------|
| OPERA    | String| Nombre de la aerolínea               | "Aerolineas Argentinas"    |
| TIPOVUELO| String| Tipo de vuelo ("N" o "I")             | "N"                        |
| MES      | Int   | Mes del vuelo (1-12)                  | 3                          |
| Fecha-I  | String| Fecha y hora inicial del vuelo        | "2025-01-01 00:00:00"      |
| Fecha-O  | String| Fecha y hora programada del vuelo     | "2025-01-01 02:00:00"      |
| SIGLAORI | String| Código del aeropuerto de origen       | "SCL"                      |
| SIGLADES | String| Código del aeropuerto de destino      | "EZE"                      |
| DIANOM   | String| Día de la semana                      | "Lunes"                    |
| Vlo-I    | String| Código del vuelo                      | "AR1234"                    |
| Emp-I    | String| Código de la empresa operadora        | "AR"                        |

### Ejemplo de consulta con `curl`

```bash
curl -X POST "https://latam-api-700756977721.us-central1.run.app/predict" \
     -H "Content-Type: application/json" \
     -d '{
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
       }'
```
Respuesta esperada

Si la solicitud es exitosa, la API devolverá una respuesta en formato JSON similar a la siguiente:

{
   "predict": [0]
}

En caso de errores, como datos faltantes o mal formateados, se recibirá una respuesta HTTP 422 con detalles del problema:

{
   "detail": "Faltan columnas: ['Fecha-O']"
}

Pruebas adicionales

Se recomienda utilizar herramientas como Postman para realizar pruebas adicionales, o incluir el script de prueba automatizado en el flujo de CI/CD para verificar la disponibilidad y precisión de la API.

Puedes agregar este apartado al documento para proporcionar instrucciones claras sobre el consumo de la API y facilitar su uso a otros desarrolladores o testers.

## 🏁 Conclusines.

### **Principales Hallazgos y Retos Superados**

**Problemas con dependencias y compatibilidad:**

* Se detectaron múltiples conflictos entre versiones de librerías y Python.
* Se crearon entornos virtuales específicos para cada parte del proyecto.
* Desafíos en el modelo de machine learning:

* Ajuste fino de los parámetros del modelo para obtener un balance entre precisión y recall.
* Adaptación de pruebas de validación para que el modelo respondiera según las expectativas del negocio.

**Problemas con GitHub y despliegue:**

- Fallos recurrentes al realizar git push debido a límites de tamaño y errores de autenticación.
- Se migró a SSH para mejorar la conectividad y autenticación segura.

**Despliegue manual vs automatizado:**

Se propone la implementación de Terraform para una gestión más eficiente, pero debido a limitaciones de tiempo se optó por despliegues manuales utilizando GCP CLI.

Este desafío ha permitido demostrar la capacidad de:

- 🔹 Transcribir y mejorar modelos de Machine Learning.
- 🔹 Desarrollar APIs escalables usando FastAPI.
- 🔹 Implementar despliegues en Google Cloud Run.
- 🔹 Automatizar flujos de CI/CD con GitHub Actions.

---
# **Propuesta de Uso para LATAM Airlines**

El modelo de predicción de atrasos puede ser utilizado por LATAM Airlines en el Aeropuerto de Santiago para:

**Optimización de operaciones:** Planificación de vuelos con base en predicciones de atrasos, reduciendo tiempos de espera y optimizando el uso de recursos.
**Comunicación con pasajeros:** Proporcionar información anticipada sobre posibles retrasos, mejorando la experiencia del cliente.
**Gestión de tripulación:** Ajustar turnos y descansos de la tripulación en función de los tiempos estimados de retraso.
Análisis de patrones: Identificación de factores recurrentes que afectan la puntualidad, como condiciones meteorológicas o congestión del aeropuerto.

## Comentarios Finales:
Este desafío ha sido una excelente oportunidad para poner a prueba las habilidades prácticas de un **Ingeniero de Machine Learning** con experiencia, ya que abarca todo el ciclo de vida de un modelo, desde la concepción hasta su despliegue en producción. A lo largo de este proceso, se enfrentaron diversos retos técnicos que van más allá del simple entrenamiento de un modelo, demostrando que el verdadero valor de un ML Engineer radica en su capacidad para integrar múltiples disciplinas, gestionar problemas inesperados y garantizar la operatividad del sistema en entornos reales.

Uno de los mayores aprendizajes de este desafío es la importancia de la **adaptabilidad y el pensamiento crítico**, dado que el despliegue de modelos de Machine Learning en entornos productivos rara vez ocurre sin contratiempos. Se presentaron desafíos relacionados con la compatibilidad de dependencias, la **optimización del modelo para un entorno de producción con recursos limitados**, la automatización del proceso de integración y despliegue continuo (CI/CD), y la **gestión eficiente de la infraestructura en la nube**. Superar estos obstáculos requirió no solo habilidades técnicas avanzadas, sino también una comprensión profunda de los procesos operativos y la capacidad de tomar decisiones informadas bajo presión.

Además, este ejercicio ha resaltado la importancia de la **colaboración y la comunicación entre equipos multidisciplinarios**. Un modelo de Machine Learning exitoso no solo debe ofrecer buenas métricas de precisión, sino que también debe alinearse con los objetivos del negocio, integrarse adecuadamente en los sistemas existentes y ser fácilmente operable por los stakeholders. La documentación clara, el versionado adecuado del código, y la **implementación de buenas prácticas de MLOps** son aspectos clave que garantizan la mantenibilidad y escalabilidad de la solución.

Finalmente, el desafío refuerza la idea de que el rol del Ingeniero de Machine Learning no termina cuando el modelo está entrenado, sino que apenas comienza. La **capacidad de desplegar, monitorear y mejorar continuamente el modelo** en respuesta a cambios en los datos y las necesidades del negocio es lo que realmente diferencia a un profesional experimentado en el campo. Este tipo de retos proporcionan una **comprensión holística del proceso de producción de modelos de Machine Learning**, preparando al ingeniero para enfrentar escenarios complejos del mundo real con confianza y eficiencia.

## 🚀 Envío del desafío

Se realizó el envío de la solución mediante la siguiente petición POST:

```bash
curl -X POST https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/software-engineer \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Fernando Nachbauer",
           "mail": "fernachbauer@gmail.com",
           "github_url": "https://github.com/fernachbauer/latam-mle-challenge.git",
           "api_url": "https://latam-api-700756977721.us-central1.run.app"
         }'
```


¡Gracias por la oportunidad de participar en este desafío! 🎉 Si tienen alguna pregunta, estaré encantado de responder. 🤓
¡ Nos vemos en las nubes!
       __|__
--@--@--(_)--@--@--
