personaje = {
    "nombre": "Braulio",
    "jugador": "Bruno"
    }

print("--------------------")

for llave in personaje:
    print("Llave:", llave)
    print("Valor:", personaje[llave])

print("--------------------")
print("  .keys")

for i in personaje.keys():
    print(i)

print("--------------------")
print("  .values")

for i in personaje.values():
    print(i)

print("--------------------")
print("  .items")

for l, v in personaje.items():
    print(l, v)

print("--------------------")