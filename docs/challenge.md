# 🚀 Desafío Software Engineer (ML & LLMs) - Entrega Final

¡Hola equipo! 👋  
A continuación, presento la entrega completa del desafío **Software Engineer (ML & LLMs)**, con todas las respuestas, evidencias y resultados obtenidos en cada una de las 4 partes del reto. 🎯

## 👤​ Información General

**Participante:** Fernando Nachbauer

**Correo:** fernachbauer@gmail.com

**Repositorio GitHub:** latam-mle-challenge

**URL de la API desplegada:** [latam-api](https://latam-api-700756977721.us-central1.run.app/health)

---

## 📝 Índice

1. [Resumen del Desafío](#resumen-del-desafío)
2. [Evidencia del proyecto](#Evidencia-del-proyecto)
3. [Parte 1: Transcripción del modelo](#parte-1-transcripción-del-modelo)
4. [Parte 2: Implementación de la API con FastAPI](#parte-2-implementación-de-la-api-con-fastapi)
5. [Parte 3: Despliegue en Google Cloud](#parte-3-despliegue-en-google-cloud)
6. [Parte 4: Implementación CI/CD](#parte-4-implementación-cicd)
7. [Conclusión](#conclusión)

---

## 🛠 1. Resumen del Desafío

En este desafío, el objetivo fue operacionalizar un modelo de Machine Learning para predecir la probabilidad de **retraso de vuelos en el aeropuerto de SCL** mediante una API en FastAPI, con despliegue en Google Cloud Run y un flujo de CI/CD en GitHub Actions. Se llevaron a cabo las siguientes etapas:

A. **Transcripción del modelo de Jupyter Notebook a un script Python (model.py)** 🐍
B. **Desarrollo de una API REST con FastAPI** ⚡
C. **Despliegue de la API en Google Cloud Run** ☁️
D. **Implementación de CI/CD con GitHub Actions** 🤖

---
### 🛠 1.1 Tecnologías Utilizadas

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

## 2. 📸 Evidencias del proyecto

---

### **2.1 Validación del estado del repositorio**
```bash
git status
git log --oneline -n 5
```
📌 **Evidencia esperada:**
- Estado del repositorio (`git status`)
- Últimos 5 commits (`git log`)

<img width="588" alt="Captura de pantalla 2025-03-03 a la(s) 10 19 17" src="https://github.com/user-attachments/assets/49a61155-1ad1-45b9-8391-ec4beaf4116d" />


---

### ** 2.2 Prueba de la API en Cloud Run**

#### **2.2.1 Verificación que la API está en ejecución**
```bash
gcloud run services list
```
📌 **Evidencia esperada:**
- Listado de servicios en Google Cloud Run

<img width="674" alt="Captura de pantalla 2025-03-03 a la(s) 10 34 24" src="https://github.com/user-attachments/assets/d69571e0-4fa2-45bb-ac45-ce773292b3a5" />

- La URL del servicio en ejecución: https://latam-api-700756977721.us-central1.run.app


#### **2.2.2 Prueba de salud del servicio (`/health`)**
```bash
curl -X GET "https://latam-api-700756977721.us-central1.run.app/health"
```
📌 **Evidencia esperada:**
```json
{"status":"OK"}
```
<img width="926" alt="Captura de pantalla 2025-03-03 a la(s) 10 38 37" src="https://github.com/user-attachments/assets/a5b2ae2d-3209-4cb8-9e6d-0247103c6d0a" />

#### **2.2.3 Prueba de predicción (`/predict`)**
```bash
curl -X POST "https://latam-api-700756977721.us-central1.run.app/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "flights": [
               {
                   "OPERA": "LATAM",
                   "TIPOVUELO": "N",
                   "MES": 5,
                   "Fecha-I": "2025-05-10 18:00:00",
                   "Fecha-O": "2025-05-10 19:30:00",
                   "SIGLAORI": "SCL",
                   "SIGLADES": "MIA",
                   "DIANOM": "Viernes",
                   "Vlo-I": "LA800",
                   "Emp-I": "LA"
               }
           ]
       }'
```
📌 **Evidencia esperada:**
```json
{"predict":[0]}
```
<img width="953" alt="Captura de pantalla 2025-03-03 a la(s) 10 47 11" src="https://github.com/user-attachments/assets/fca88bdb-2d83-4cd4-b3b2-02e1f478c478" />

---

### **2.3 Validación de los contenedores y las imágenes Docker**
#### **2.3.1 Verificar las imágenes en Google Container Registry**
```bash
gcloud container images list
```
📌 **Evidencia esperada:**
- Listado de imágenes en GCR

<img width="823" alt="Captura de pantalla 2025-03-03 a la(s) 10 49 07" src="https://github.com/user-attachments/assets/1edb532a-81e6-4e17-8b6b-6a81036b0428" />


### **2.4 Validación del flujo de CI/CD en GitHub Actions**
```bash
curl -s https://api.github.com/repos/fernachbauer/latam-mle-challenge/actions/runs | jq '.workflow_runs[] | {name: .name, status: .status, conclusion: .conclusion, created_at: .created_at}' | head -n 20
```
📌 **Evidencia esperada:**
- Estado de los workflows en GitHub Actions

<img width="1337" alt="Captura de pantalla 2025-03-03 a la(s) 10 54 54" src="https://github.com/user-attachments/assets/c5aced13-79af-4d03-9b3e-a3f2cc3dd0e3" />

Tambien se puede revisar manualmente en [GitHub Actions](https://github.com/fernachbauer/latam-mle-challenge/actions).

---

### **2.5 Ejecución de pruebas unitarias**
```bash
pytest tests/api/test_api.py
pytest tests/model/test_model.py
```
📌 **Evidencia esperada:**
- Pruebas exitosas con `pytest`

<img width="1417" alt="Captura de pantalla 2025-03-03 a la(s) 10 58 32" src="https://github.com/user-attachments/assets/489b9647-cfad-4bd1-a1b3-7eead3d6da05" />

<img width="1415" alt="Captura de pantalla 2025-03-03 a la(s) 11 01 42" src="https://github.com/user-attachments/assets/ca73a72a-a9c6-43d2-8c8e-0dc875840b3c" />


---

### **2.6 Envío del proyecto**
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
📌 **Evidencia esperada:**
```json
{
  "status": "OK",
  "detail": "your request was received"
}
```
<img width="570" alt="Captura de pantalla 2025-03-02 a la(s) 20 15 02" src="https://github.com/user-attachments/assets/24d48ac0-fe60-4473-9193-7794db5bc4dd" />

---

### **2.8 Lista de documentación adjunta de los resultados**

Se adjuntaton las capturas de pantalla de cada paso y se agregaron al documento de entrega.

📌 **Checklist de Evidencias:**
✅ `git status` y `git log`  
✅ `gcloud run services list`  
✅ `curl -X GET` `/health`  
✅ `curl -X POST` `/predict`  
✅ `gcloud container images list`   
✅ `pytest` para API y modelo  
✅ `curl -X POST` para enviar el challenge  

---
# Desarrollo del Proyecto
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
   

<img width="943" alt="Captura de pantalla 2025-03-03 a la(s) 11 32 12" src="https://github.com/user-attachments/assets/6f2c18fc-1456-47db-a171-565e39c45ef4" />

La prueba de estrés con **Locust** se ejecutó correctamente. Aquí están los principales resultados como evidencia:

---

### 📊 **Resultados del Test de Estrés**
**Configuración del test:**
- **URL del servicio:** [latam-api-700756977721.us-central1.run.app](https://latam-api-700756977721.us-central1.run.app)
- **Duración:** 60 segundos
- **Usuarios simultáneos:** 100
- **Frecuencia de generación de usuarios:** 1 usuario por segundo
- **Tipo de solicitud:** `POST /predict`
- **Número total de peticiones:** `2,278`
- **Errores:** `0 (0.00%)`
- **Latencia promedio:** `741ms`
- **Latencia mínima:** `59ms`
- **Latencia máxima:** `11,000ms`
- **Percentiles de respuesta:**
  - **50% (mediana):** `560ms`
  - **75%:** `1,100ms`
  - **90%:** `1,700ms`
  - **99.9%:** `9,000ms`


### ✅ **Conclusión**
El API **latam-api** maneja correctamente 100 usuarios concurrentes con más de **2,200 requests** en un minuto sin fallos. Sin embargo, hay algunas latencias altas en percentiles altos (p99.9 > 9s), lo que indica que podría haber optimizaciones en infraestructura o código.

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

---

¡Gracias por la oportunidad de participar en este desafío! 🎉 

Si tienen alguna pregunta, estaré encantado de responder. 🤓

**¡ Nos vemos en las nubes!**


       __|__
--@--@--(_)--@--@--


