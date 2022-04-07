import sys
import os

# indicamos la carpeta del proyecto para importar la clases correctamente
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

    def agregar(self, empleado):
        self.empleadoDao.agregar(empleado)

    def actualizar(self, empleado):
        self.empleadoDao.actualizar(empleado)

    def borrar(self, empleado):
        self.empleadoDao.borrar(empleado)