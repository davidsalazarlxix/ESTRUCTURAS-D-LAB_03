# Ordenacion por seleccion
def seleccion_por_orden(s, i=0):
    if i >= len(s) - 1:
        return
    m = min(range(i, len(s)), key=lambda k: s[k])
    s[i], s[m] = s[m], s[i]
    seleccion_por_orden(s, i + 1)

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    seleccion_por_orden(arr)
    print("Arreglo ordenado:", arr)
