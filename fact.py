# Clase Factura
class Factura:
    def __init__(self, numero, cliente, fecha):
        self.numero = numero  # Número de la factura
        self.cliente = cliente  # Nombre del cliente
        self.fecha = fecha  # Fecha de emisión de la factura
        self.monto_total = 0  # Monto total de la factura, inicializado a 0
        self.items = []  # Lista para almacenar los productos/servicios de la factura

    def agregar_item(self, descripcion, cantidad, precio_unitario):
        """Añade un producto o servicio a la factura y actualiza el monto total"""
        item_total = cantidad * precio_unitario
        self.items.append({
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio_unitario': precio_unitario,
            'item_total': item_total
        })
        self.monto_total += item_total
        print(f"Se ha agregado el producto/servicio '{descripcion}' por un total de ${item_total:.2f}")

    def mostrar_detalles(self):
        """Imprime los detalles completos de la factura"""
        print(f"Factura número: {self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print("Detalles de los items:")
        for item in self.items:
            print(f"- {item['descripcion']} | Cantidad: {item['cantidad']} | Precio unitario: ${item['precio_unitario']:.2f} | Total: ${item['item_total']:.2f}")
        print(f"Monto total: ${self.monto_total:.2f}")

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al monto total"""
        descuento = (self.monto_total * porcentaje) / 100
        self.monto_total -= descuento
        print(f"Se ha aplicado un descuento del {porcentaje}%: ${descuento:.2f}")
        print(f"Nuevo monto total después del descuento: ${self.monto_total:.2f}")

# Ejemplo de uso

# Crear una factura
factura1 = Factura(1001, "Juan Pérez", "2024-11-24")

# Agregar productos a la factura
factura1.agregar_item("Laptop", 1, 1200.00)
factura1.agregar_item("Ratón inalámbrico", 2, 25.00)
factura1.agregar_item("Teclado mecánico", 1, 150.00)

# Mostrar los detalles de la factura
factura1.mostrar_detalles()

# Aplicar un descuento del 10% a la factura
factura1.aplicar_descuento(10)

# Mostrar los detalles de la factura después del descuento
factura1.mostrar_detalles()
