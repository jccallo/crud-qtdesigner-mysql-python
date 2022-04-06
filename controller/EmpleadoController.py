import sys
import os

# indicamos la carpeta del proyecto para impotar la clases correctamente
proyecto = os.getcwd()
sys.path.append("..")
sys.path.append(proyecto)

# importamos EmpleadoDao
from model.EmpleadoDao import EmpleadoDao

class EmpleadoController():
    def __init__(self):
        self.empleadoDao = EmpleadoDao()

    def obtenerTodos(self):
        return self.empleadoDao.obtenerTodos()

