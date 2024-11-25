# Clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje_descuento):
        """Aplica un descuento al precio del libro"""
        descuento = (self.precio * porcentaje_descuento) / 100
        self.precio -= descuento
        print(f"Descuento de {porcentaje_descuento}% aplicado. El nuevo precio de '{self.titulo}' es ${self.precio:.2f}")

    def mostrar_informacion(self):
        """Muestra los detalles completos del libro"""
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Precio: ${self.precio:.2f}")

    def es_mas_caro_que(self, otro_libro):
        """Compara los precios entre dos libros y devuelve el más caro"""
        if self.precio > otro_libro.precio:
            return self
        else:
            return otro_libro

# Ejemplo de uso

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 25.00)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Ficción", 30.00)

# Mostrar la información de los libros
libro1.mostrar_informacion()
libro2.mostrar_informacion()

# Aplicar descuento en el libro 1
libro1.aplicar_descuento(15)  # Descuento del 15%

# Comparar los precios de los libros
libro_mas_caro = libro1.es_mas_caro_que(libro2)

# Mostrar el libro más caro
print(f"\nEl libro más caro es: '{libro_mas_caro.titulo}' con un precio de ${libro_mas_caro.precio:.2f}")
