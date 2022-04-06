import pymysql

class EmpleadoDao():
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="Mysql2004",
            database="database_empleados"
        )

    def createTable(self):
        sql = """
            CREATE TABLE empleados (
                id INT NOT NULL AUTO_INCREMENT,
                codigo varchar(50),
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
            sql = """SELECT * FROM empleados"""
            cursor.execute(sql)
            empleados = cursor.fetchall()
            cursor.close()
            return empleados



