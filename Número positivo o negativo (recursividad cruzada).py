# Actividad 1.8: Número positivo o negativo (recursividad cruzada)
def positivo(n):
    if n < 0:
        return False
    return not negativo(n)

def negativo(n):
    if n >= 0:
        return False
    return not positivo(n)

if __name__ == "__main__":
    for x in (5, -3, 0):
        print(x, "-> positivo:", positivo(x), "| negativo:", negativo(x))