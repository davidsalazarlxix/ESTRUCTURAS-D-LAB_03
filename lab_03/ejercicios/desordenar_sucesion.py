# Desordenar una sucesion (Fisher-Yates)
import random

def desordena(a, i=0):
    if i >= len(a) - 1:
        return
    k = random.randint(i, len(a) - 1)
    a[i], a[k] = a[k], a[i]
    desordena(a, i + 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    desordena(arr)
    print("Arreglo desordenado:", arr)
