# Prueba Chi-Cuadrado de aleatoriedad
import random
from collections import Counter

def desordena(a, i=0):
    if i >= len(a) - 1:
        return
    k = random.randint(i, len(a) - 1)
    a[i], a[k] = a[k], a[i]
    desordena(a, i + 1)

def prueba_aleatoriedad(n_pruebas=60000):
    cont = Counter()
    for _ in range(n_pruebas):
        arr = [1, 2, 3]
        desordena(arr)
        cont[tuple(arr)] += 1

    esperado = n_pruebas / 6
    chi2 = 0
    for p in sorted(cont):
        chi2 += (cont[p] - esperado) ** 2 / esperado
    return chi2

if __name__ == "__main__":
    print("Resultado Chi-Cuadrado:", prueba_aleatoriedad())
