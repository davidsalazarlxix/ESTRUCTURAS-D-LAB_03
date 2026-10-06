# Actividad 1.5: Suma de los elementos de un vector
def suma_vec(v, n):
    if n == 0:
        return v[0]
    return suma_vec(v, n - 1) + v[n]

if __name__ == "__main__":
    v = [2, 4, 6, 8]
    print(suma_vec(v, len(v) - 1))