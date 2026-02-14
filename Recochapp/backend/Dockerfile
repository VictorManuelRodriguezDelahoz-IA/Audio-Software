FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2 (Postgres)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copiar dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY . .

# El comando se define en docker-compose, pero este es el default
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]