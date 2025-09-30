class Persona:
    def __init__(self, nombre, edad):
        print(f">>> Constructor de Persona <{nombre}> ejecutado.")
        self.name = nombre
        self.age = edad
        print("--------------------")
    
    def cumplir_anios(self):
        print(f">>> Función de Persona <{self.name}> ejecutada.")
        self.age += 1
        print(f"Feliz cumpleaños #{self.age} {self.name}")
        print("--------------------")

#   Sin el <super>:
"""
class Empleado(Persona):
    def tabajar(self, hs_trabajadas):
        print(f">>> Función de Empleado <{self.name}> ejecutada.")
        print(f"{self.name} trabajó {hs_trabajadas} horas")
        print("--------------------")
"""
#   Con el <super>:

class Empleado(Persona):
    def __init__(self, hs_totales, nombre, edad):
        super(Empleado, self).__init__(nombre, edad)
        print(f">>> Constructor de Empleado <{self.name}> ejecutado.")
        self.total = hs_totales
        print("--------------------")

    def tabajar(self, hs_trabajadas):
        print(f">>> Función de Empleado <{self.name}> ejecutada.")
        print(f"{self.name} trabajó {hs_trabajadas} horas")
        print("--------------------")
        self.total += hs_trabajadas
        print("Horas totales:", self.total)
        print("--------------------")

print("----------------------------------------")

#bruno = Empleado("Bruno", 28)
bruno = Empleado(nombre="Bruno",edad=28,hs_totales=100)

bruno.tabajar(8)
bruno.cumplir_anios()