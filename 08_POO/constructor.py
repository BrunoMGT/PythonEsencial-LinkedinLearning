class Persona:
    def __init__(self):
        print("Esto es el constructor")

print("--------------------")

Bruno = Persona()
Deborah = Persona()

print("--------------------")

print("El tipo de Bruno es", type(Bruno))
print("El tipo de Deborah es", type(Deborah))

print()

print("¿Son el mismo elemento? ->", Bruno==Deborah)
print("¿Son del mismo tipo? ->", type(Bruno)==type(Deborah))

print("--------------------")