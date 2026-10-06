# Actividad 1.9: Número impar con recursividad cruzada
def par(n):
    if n == 0:
        return True
    return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    return par(n - 1)

if __name__ == "__main__":
    print("impar(7):", impar(7))
    print("impar(10):", impar(10))
    print("par(10):", par(10))