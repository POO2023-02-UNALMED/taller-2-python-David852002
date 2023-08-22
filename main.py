class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo in ["gasolina", "electrico"]:
            self.tipo = tipo


class Auto:
    def __init__(self, modelo,precio,marca,motor,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        Asiento.asientos = []
        self.marca = marca
        Motor.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados
    
    def cantidadAsientos(self):
        contador = 0
        for asiento in Asiento.asiento:
            if asiento is not None:
                contador += 1
            return contador
    
    def verificarIntegridad(self):
        if self.registro == Motor.registro:
            for asiento in Asiento.asientos:
                if asiento is not None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"