# Usa una imagen base liviana con Python
FROM python:3.10-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala dependencias del sistema necesarias para PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia todo el código del proyecto al contenedor
COPY . .

# Recolectar archivos estáticos al construir la imagen
RUN python manage.py collectstatic --noinput

# Comando por defecto: usar Gunicorn como servidor WSGI
CMD ["gunicorn", "tickets_3J.wsgi:application", "--bind", "0.0.0.0:8000"]
