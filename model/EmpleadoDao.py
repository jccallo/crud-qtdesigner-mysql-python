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
        # la conexion de a una una base de datos mysql
        self.conexion = mysql.connector.connect(
            host="localhost", # nombre del server o host
            user="root", # nombre usuario
            password="Mysql2004", # contraseña
            database="database_empleados" # nombre de la base de datos
        )

    # para crear la tabla desde la clase (opcional porque se puede crear manualmente)
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
        cursor = self.conexion.cursor() # apuntamos a la base de datos
        sql = "SELECT * FROM empleados" # consulta sql que queremos hacer
        cursor.execute(sql) # ejecutamos la consulta
        empleados = cursor.fetchall() # guardamos el resultado
        cursor.close() # cerramos conexion
        return Empleado().getLista(empleados) # lo transformamos a una lista de objetos Empleados 

    def agregar(self, empleado):
        cursor = self.conexion.cursor() # apuntamos a la base de datos
        sql = """INSERT INTO empleados (nombre,dni,numero_horas,tarifa_hora) VALUES (%s,%s,%s,%s)""" # consulta sql que queremos hacer
        
        # pasamos la consulta y tambien una tupla de valores del empleado que se reemplazará en la consulta
        cursor.execute(sql, ( 
            empleado.getNombre(), 
            empleado.getDni(), 
            empleado.getNumeroHoras(), 
            empleado.getTarifaHora()
        ))
        self.conexion.commit() # aceptar los cambios hechos en la base de datos
        cursor.close() # cerramos conexion

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
        cursor.execute(sql, (empleado.getId(),)) # tupla de un solo elemento
        self.conexion.commit()
        cursor.close()


