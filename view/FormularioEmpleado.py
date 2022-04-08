import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic

# indicamos la carpeta del proyecto para importar la clases correctamente
proyecto = os.getcwd()
sys.path.append("..")
sys.path.append(proyecto)

# importamos al controlador
from controller.EmpleadoController import EmpleadoController
from model.Empleado import Empleado

class FormularioEmpleados(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/FormularioEmpleado.ui", self)  # cargamos la interfaz
        self.empleadoController = EmpleadoController()  # instanciamos el contralador
        
        # botones y los eventos
        self.btnListar.clicked.connect(self.listar)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.btnBorrar.clicked.connect(self.borrar)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.tbwListado.clicked.connect(self.llenarCampos)

        # damos tamaño a las columnas de la tabla
        for indice, ancho in enumerate((50, 108, 73, 60, 78), start=0):
            self.tbwListado.setColumnWidth(indice, ancho)

    def listar(self):
        # obtenemos los empleados
        empleados = self.empleadoController.obtenerTodos() 

        # cargamos los empleados en la tabla
        fila = 0
        for empleado in empleados:
            self.tbwListado.setRowCount(fila + 1)
            self.tbwListado.setItem(fila, 0, QTableWidgetItem(str(empleado.getId())))
            self.tbwListado.setItem(fila, 1, QTableWidgetItem(empleado.getNombre()))
            self.tbwListado.setItem(fila, 2, QTableWidgetItem(empleado.getDni()))
            self.tbwListado.setItem(fila, 3, QTableWidgetItem(str(empleado.getNumeroHoras())))
            self.tbwListado.setItem(fila, 4, QTableWidgetItem(str(empleado.getTarifaHora())))
            fila += 1
        
    def agregar(self):
        # instanciamos un objeto empleado y setemos los campos necesario
        empleado = Empleado()
        empleado.setNombre(self.txtNombre.text())
        empleado.setDni(self.txtDni.text())
        empleado.setNumeroHoras(int(self.spbNumeroHoras.text()))
        empleado.setTarifaHora(float(self.spbTarifaHora.text()))

        # agregamos un empleado
        self.empleadoController.agregar(empleado)

        # listamos los empleados en la tabla 
        self.listar()

        # limpiamos los campos
        self.nuevo()

    def actualizar(self):
        # verificamos si el campo de Id este llenado con un numero
        if not self.txtId.text().isnumeric():
            return 

        # obtenemos el empleado con los datos de los campos
        empleado = self.obtenerActualEmpleado()

        # actualizamos un empleado
        self.empleadoController.actualizar(empleado)

        # listamos los empleados en la tabla 
        self.listar()

    def borrar(self):
        # verificamos si el campo de Id este llenado con un numero
        if not self.txtId.text().isnumeric():
            return 

        # obtenemos el empleado con los datos de los campos
        empleado = self.obtenerActualEmpleado()

        # borramos empleado
        self.empleadoController.borrar(empleado)

        # listamos los empleados en la tabla 
        self.listar()

        # listamos los empleados en la tabla 
        self.nuevo()    

    # limpia y setea todos los campos del formulario
    def nuevo(self):
        self.txtId.clear()
        self.txtNombre.clear()
        self.txtDni.clear()
        self.spbNumeroHoras.setValue(0)
        self.spbTarifaHora.setValue(0.0)
        self.txtId.setFocus()

    # setea un objeto con los datos del campo del formulario
    def obtenerActualEmpleado(self):
        empleado = Empleado()
        empleado.setId(int(self.txtId.text()))
        empleado.setNombre(self.txtNombre.text())
        empleado.setDni(self.txtDni.text())
        empleado.setNumeroHoras(int(self.spbNumeroHoras.value()))
        empleado.setTarifaHora(float(self.spbTarifaHora.value()))
        return empleado

    # llena los el formulario al hacer click a una fila de la tabla
    def llenarCampos(self):
        filaSeleccionada = self.tbwListado.selectedItems()
        self.txtId.setText(filaSeleccionada[0].text())
        self.txtNombre.setText(filaSeleccionada[1].text())
        self.txtDni.setText(filaSeleccionada[2].text())
        self.spbNumeroHoras.setValue(int(filaSeleccionada[3].text()))
        self.spbTarifaHora.setValue(float(filaSeleccionada[4].text()))

# este es el archivo principal donde ejecutamos nuestra aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv) # se crea la aplicacion
    objeto = FormularioEmpleados() # se crea el objeto de la clase
    objeto.show() # hacemos que se muestre
    sys.exit(app.exec_()) # para ejecutar y cerrar la aplicacion
