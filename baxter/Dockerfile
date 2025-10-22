# Dockerfile
FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instalación de dependencias del sistema
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    git \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiar el repositorio
COPY . /app

# Instalar Python dependencies
RUN pip install --no-cache-dir pybullet numpy

# Comando por defecto para ejecutar el script de Baxter
CMD ["python", "baxter_ik_demo.py"]
