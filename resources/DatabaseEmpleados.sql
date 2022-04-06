CREATE DATABASE database_empleados;
USE database_empleados;

CREATE TABLE empleados (
   id INT NOT NULL AUTO_INCREMENT,
   codigo varchar(50),
   nombre varchar(100),
   dni varchar(25),
   numero_horas INT,
   tarifa_hora DECIMAL(10, 2),
   CONSTRAINT pk_empleados PRIMARY KEY (id)
);