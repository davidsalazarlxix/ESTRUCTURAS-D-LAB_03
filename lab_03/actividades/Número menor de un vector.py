# Actividad 1.11: Número menor de un vector
def menor_vec(x, n):
    if n == 0:
        return x[0]
    m = menor_vec(x, n - 1)
    return x[n] if x[n] < m else m

if __name__ == "__main__":
    datos = [9, 4, 7, 1, 8]
    print(menor_vec(datos, len(datos) - 1))