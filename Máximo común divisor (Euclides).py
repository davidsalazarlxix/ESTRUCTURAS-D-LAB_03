# Actividad 1.7: Máximo común divisor (Euclides)
def sacar_mcd(a, b):
    if b == 0:
        return a
    return sacar_mcd(b, a % b)

if __name__ == "__main__":
    print(sacar_mcd(48, 18))
    print(sacar_mcd(17, 5))