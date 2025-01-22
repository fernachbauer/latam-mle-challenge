# Usar una imagen base con Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar las dependencias del proyecto
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["uvicorn", "challenge.api:app", "--host", "0.0.0.0", "--port", "8080"]
