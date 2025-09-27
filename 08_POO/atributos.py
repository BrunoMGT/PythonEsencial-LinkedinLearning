class Persona:
    atributo = 747
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad
        print("Constructor de", nombre, "ejecutado.")

print("--------------------")

bruno = Persona("Bruno", 28)
debo = Persona("Deborah", 29)

print("--------------------")
print(bruno.name, bruno.age)
print(debo.name, debo.age)
print()
print("Atributo:",bruno.atributo)
print("--------------------")