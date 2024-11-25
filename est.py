# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre  # Nombre del estudiante
        self.edad = edad  # Edad del estudiante
        self.grado = grado  # Grado escolar del estudiante
        self.materias = []  # Lista de materias inscritas por el estudiante

    def inscribir_materia(self, materia):
        """Agrega una materia a la lista de materias del estudiante"""
        self.materias.append(materia)
        print(f"{self.nombre} se ha inscrito en la materia '{materia}'.")

    def mostrar_materias(self):
        """Muestra las materias inscritas por el estudiante"""
        if self.materias:
            print(f"{self.nombre} está inscrito en las siguientes materias:")
            for materia in self.materias:
                print(f"- {materia}")
        else:
            print(f"{self.nombre} no está inscrito en ninguna materia aún.")

    def actualizar_grado(self, nuevo_grado):
        """Cambia el grado del estudiante"""
        self.grado = nuevo_grado
        print(f"{self.nombre} ha sido actualizado al grado {self.grado}.")

# Ejemplo de uso

# Crear algunos estudiantes
estudiante1 = Estudiante("Juan Pérez", 16, 10)
estudiante2 = Estudiante("Ana Gómez", 15, 9)

# Inscribir materias para los estudiantes
estudiante1.inscribir_materia("Matemáticas")
estudiante1.inscribir_materia("Historia")
estudiante2.inscribir_materia("Biología")
estudiante2.inscribir_materia("Física")

# Mostrar las materias inscritas por los estudiantes
estudiante1.mostrar_materias()
estudiante2.mostrar_materias()

# Actualizar el grado de un estudiante
estudiante1.actualizar_grado(11)

# Mostrar nuevamente las materias y el grado actualizado
estudiante1.mostrar_materias()
print(f"Grado actualizado: {estudiante1.grado}")
