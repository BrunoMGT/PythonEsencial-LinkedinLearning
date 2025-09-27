def calc_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return area, perimetro

la = 3

ar, pe = calc_cuadrado(la)
print("--------------------")
print(f"Lado: {la}")
print(f"Area: {ar}, Perímetro: {pe}")
print("--------------------")