# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # Por defecto, la habitación está disponible

    def reservar(self):
        """Marca la habitación como no disponible"""
        if self.disponible:
            self.disponible = False
            print(f"La habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Marca la habitación como disponible"""
        if not self.disponible:
            self.disponible = True
            print(f"La habitación {self.numero} ha sido liberada y ahora está disponible.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")

    def mostrar_informacion(self):
        """Muestra los detalles completos de la habitación"""
        disponibilidad = "disponible" if self.disponible else "ocupada"
        print(f"Número de habitación: {self.numero}")
        print(f"Tipo de habitación: {self.tipo}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Estado: {disponibilidad}\n")

# Ejemplo de uso

# Crear habitaciones
habitacion1 = Habitacion(101, "Individual", 75.00)
habitacion2 = Habitacion(102, "Doble", 120.00)

# Mostrar la información de las habitaciones
habitacion1.mostrar_informacion()
habitacion2.mostrar_informacion()

# Reservar una habitación
habitacion1.reservar()

# Intentar reservar la habitación que ya está ocupada
habitacion1.reservar()

# Liberar una habitación
habitacion1.liberar()

# Mostrar la información actualizada de las habitaciones
habitacion1.mostrar_informacion()
habitacion2.mostrar_informacion()
