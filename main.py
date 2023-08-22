class Asiento:
    def __init__(self):
        self.color = None
        self.precio = 0
        self.registro = 0
    
    def cambiar_color(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color


class Motor:
    def __init__(self):
        self.numero_cilindros = 0
        self.tipo = None
        self.registro = 0
    
    def cambiar_registro(self, nuevo_registro):
        self.registro = nuevo_registro
    
    def asignar_tipo(self, nuevo_tipo):
        if nuevo_tipo in ["gasolina", "electrico"]:
            self.tipo = nuevo_tipo


class Auto:
    def __init__(self):
        self.modelo = None
        self.precio = 0
        self.asientos = []
        self.marca = None
        self.motor = None
        self.registro = 0
        self.cantidad_creados = 0
    
    def cantidad_asientos(self):
        contador = 0
        for asiento in self.asientos:
            if asiento is not None:
                contador += 1
        return contador
    
    def verificar_integridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento is not None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"