import sys
import os
import mysql.connector

# indicamos la carpeta del proyecto para importar la clases correctamente
proyecto = os.getcwd()
sys.path.append("..")
sys.path.append(proyecto)

# importamos el modelo Empleado
from model.Empleado import Empleado

class EmpleadoDao():
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysql2004",
            database="database_empleados"
        )

    def createTable(self):
        sql = """
            CREATE TABLE empleados (
                id INT NOT NULL AUTO_INCREMENT,
                nombre varchar(100),
                dni varchar(25),
                numero_horas INT,
                tarifa_hora DECIMAL(10, 2),
                CONSTRAINT pk_empleados PRIMARY KEY (id)
            );
        """
        self.conexion.cursor().execute(sql)

    def obtenerTodos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM empleados"
        cursor.execute(sql)
        empleados = cursor.fetchall()
        cursor.close()
        return Empleado().getLista(empleados) 

    def agregar(self, empleado):
        cursor = self.conexion.cursor()
        sql = """INSERT INTO empleados (nombre,dni,numero_horas,tarifa_hora) VALUES (%s,%s,%s,%s)"""
        cursor.execute(sql, (
            empleado.getNombre(), 
            empleado.getDni(), 
            empleado.getNumeroHoras(), 
            empleado.getTarifaHora()
        ))
        self.conexion.commit()
        cursor.close()

    def actualizar(self, empleado):
        cursor = self.conexion.cursor()
        sql = """UPDATE empleados SET nombre = %s, dni = %s, numero_horas = %s, tarifa_hora = %s WHERE id = %s"""
        cursor.execute(sql, (
            empleado.getNombre(), 
            empleado.getDni(), 
            empleado.getNumeroHoras(), 
            empleado.getTarifaHora(),
            empleado.getId()
        ))
        self.conexion.commit()
        cursor.close()

    def borrar(self, empleado):
        cursor = self.conexion.cursor()
        sql = """DELETE FROM empleados WHERE id = %s"""
        cursor.execute(sql, (empleado.getId(),))
        self.conexion.commit()
        cursor.close()

# ed = EmpleadoDao()
# ed.agregar(Empleado("c003"))
# for x in ed.obtenerTodos():
#     print(x.getCodigo())
