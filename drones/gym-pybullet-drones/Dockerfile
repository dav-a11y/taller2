# Usamos Debian slim + Python
FROM python:3.12-slim

# Variables para no interactuar con apt
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias para OpenGL y PyBullet
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    build-essential \
    libgl1 \
    libgl1-mesa-dri \
    libx11-dev \
    libxrandr-dev \
    libxi-dev \
    libxinerama-dev \
    libxcursor-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar el repositorio completo
COPY . /app

# Instalar gym-pybullet-drones
RUN pip install --upgrade pip setuptools wheel
RUN pip install .

# Establecer variable para GUI
ENV DISPLAY=:0
