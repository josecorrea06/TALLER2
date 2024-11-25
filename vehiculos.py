# Clase base
class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        """Muestra los detalles básicos del vehículo"""
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")

# Clases hijas

class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        """Muestra los detalles del coche de F1, incluyendo tipo de neumáticos"""
        super().mostrar_info()
        print(f"Tipo de neumáticos: {self.tipo_neumaticos}\n")

class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        """Muestra los detalles de la moto de GP, incluyendo tipo de carenado"""
        super().mostrar_info()
        print(f"Tipo de carenado: {self.tipo_carenado}\n")

# Ejemplo de uso

# Crear algunos vehículos de carreras
coche_f1 = CocheF1("Ferrari", "SF-23", 360, "Neumáticos blandos")
moto_gp = MotoGP("Yamaha", "YZR-M1", 350, "Carenado aerodinámico")

# Mostrar la información de los vehículos
coche_f1.mostrar_info()
moto_gp.mostrar_info()
