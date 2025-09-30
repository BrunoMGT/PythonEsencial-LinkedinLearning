class Persona:
    atributo = 747
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad
        print("Constructor de", nombre, "ejecutado.")
    
    def cumplir_anios(self):
        self.age += 1
        print(f"Feliz cumpleaños #{self.age} {self.name}")
        print("--------------------")

print("--------------------")

bruno = Persona("Bruno", 28)
debo = Persona("Deborah", 29)

print("--------------------")
print(bruno.name, bruno.age)
print(debo.name, debo.age)
print()
print("Atributo:",bruno.atributo)
print("--------------------")

bruno.cumplir_anios()