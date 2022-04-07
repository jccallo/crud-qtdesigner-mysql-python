class Empleado:
    def __init__(self, id = 0, nombre = "", dni = "", numeroHoras = 0, tarifaHora = 0.0):
        self.__id = id
        self.__nombre = nombre
        self.__dni = dni
        self.__numeroHoras = numeroHoras
        self.__tarifaHora = tarifaHora

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def getNumeroHoras(self):
        return self.__numeroHoras

    def setNumeroHoras(self, numeroHoras):
        self.__numeroHoras = numeroHoras

    def getTarifaHora(self):
        return self.__tarifaHora

    def setTarifaHora(self, tarifaHora):
        self.__tarifaHora = tarifaHora

    def getLista(self, empleados):
        listaEmpleados = []
        for empleado in empleados:
            listaEmpleados.append(Empleado(empleado[0], empleado[1], empleado[2], empleado[3], empleado[4]))
        return listaEmpleados


# ep = Empleado('aaa', 'bbb', '123', 12, 123.4)
# print(ep.getTarifaHora())
# ep.setTarifaHora('q1q1q1')
# print(ep.getTarifaHora())
