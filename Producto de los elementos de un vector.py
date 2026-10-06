# Actividad 1.6: Producto de los elementos de un vector
def multiplicar(vec, tam):
    if tam == 0:
        return vec[0]
    return vec[tam] * multiplicar(vec, tam - 1)

if __name__ == "__main__":
    v = [1, 2, 3, 4]
    print(multiplicar(v, len(v) - 1))