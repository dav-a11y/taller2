# Simulación de Robots en PyBullet mediante Contenedores Docker  
### Casos de Estudio: Atlas, Baxter y Drones

**Autor:** David Diaz  
**Fecha:** 22 octubre 2025  
**Tipo de documento:** Informe técnico (LaTeX)

---

## Descripción General

Este proyecto documenta el proceso de **construcción, configuración y despliegue de simulaciones** de los robots **Atlas**, **Baxter** y **Drones** utilizando el entorno de física **PyBullet** dentro de **contenedores Docker**.

El objetivo es **garantizar un entorno reproducible, portable y libre de dependencias externas**, de modo que cualquier usuario pueda ejecutar las simulaciones sin configurar manualmente librerías ni entornos locales.

---

## Contenido del Documento

El informe técnico (`informe_docker_pybullet.tex`) contiene las siguientes secciones:

1. **Simulación del robot Atlas**
   - Descarga de archivos URDF desde el repositorio oficial de PyBullet.
   - Construcción de la imagen Docker (`Dockerfile1`).
   - Ejecución del contenedor con soporte gráfico (X11).
   - Visualización del robot Atlas en la GUI de PyBullet.

2. **Simulación del robot Baxter**
   - Obtención del modelo Baxter desde el repositorio de Erwin Coumans.
   - Estructura del proyecto y `Dockerfile` base.
   - Ejecución de la simulación `baxter_ik_demo.py` dentro de Docker.

3. **Simulación de drones (gym-pybullet-drones)**
   - Clonación del repositorio de la Universidad de Toronto.
   - Construcción del contenedor `gp-drones-gui`.
   - Ejecución de la simulación PID con visualización 3D.
   - Ejemplo de comando con interfaz gráfica activa.

4. **Conclusiones**
   - Se valida la portabilidad y estabilidad del entorno Docker para simulaciones robóticas reproducibles.

---

## Requisitos Previos

- Docker instalado en el sistema host.  
- Acceso a interfaz gráfica (X11 o Wayland).  
- Conexión a internet para descargar repositorios.  

---

[Overleaf](https://www.overleaf.com/read/bscydftqqbnm#9e2aad)

---

## Ejecución Rápida (Ejemplo Atlas)

```bash
# Habilitar acceso gráfico
xhost +local:root

# Construir imagen
sudo docker build -t atlas-pybullet -f Dockerfile1 .

# Ejecutar simulación
docker run -it --rm \
  --env="DISPLAY" \
  --net=host \
  --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
  atlas-pybullet

## Informe técnico: Simulación de Robots en Docker

Documento LaTeX disponible en Overleaf:



