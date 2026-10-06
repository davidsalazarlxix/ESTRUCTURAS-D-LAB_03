# Ordenacion por insercion
def insertar(s, j, val):
    if j >= 0 and val < s[j]:
        s[j + 1] = s[j]
        insertar(s, j - 1, val)
    else:
        s[j + 1] = val

def insercion_por_orden(s, n):
    if n <= 1:
        return
    insercion_por_orden(s, n - 1)
    insertar(s, n - 2, s[n - 1])

if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    insercion_por_orden(arr, len(arr))
    print("Arreglo ordenado:", arr)
