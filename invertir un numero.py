# Actividad 1.3: Invertir un número
def invertir(n, acc=0):
    if n == 0:
        return acc
    return invertir(n // 10, acc * 10 + n % 10)

if __name__ == "__main__":
    print(invertir(8435))