import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

# indicamos la carpeta del proyecto
proyecto = os.getcwd()
sys.path.append("..")
sys.path.append(proyecto)

# importamos al controlador
from controller.EmpleadoController import EmpleadoController

class FormularioEmpleados(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/FormularioEmpleado.ui",
                   self)  # cargamos la interfaz
        self.empleadoController = EmpleadoController()  # instanciamos el contralador
        self.btnListar.clicked.connect(self.listar)

    def listar(self):
        empleados = self.empleadoController.obtenerTodos()
        print(empleados)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    objeto = FormularioEmpleados()
    objeto.show()
    sys.exit(app.exec_())
