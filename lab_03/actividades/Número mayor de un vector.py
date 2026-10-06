# Actividad 1.12: Número mayor de un vector
def mayor_vec(x, n):
    if n == 0:
        return x[0]
    m = mayor_vec(x, n - 1)
    return x[n] if x[n] > m else m

if __name__ == "__main__":
    datos = [9, 4, 7, 1, 8]
    print(mayor_vec(datos, len(datos) - 1))