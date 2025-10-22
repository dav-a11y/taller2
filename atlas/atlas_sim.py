import pybullet as p
import pybullet_data
import time
from atlas import Atlas  # Asegúrate que Atlas esté definido en atlas.py

# Conectar con PyBullet
physicsClient = p.connect(p.GUI)  # p.DIRECT para sin GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Cargar el robot ATLAS
atlas_robot = Atlas()
atlas_robot.load()

# Simulación básica
for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)

# Desconectar
p.disconnect()
