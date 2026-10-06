# Elemento mayor de una sucesion
def maximo(s, n):
    if n == 1:
        return s[0]
    m = maximo(s, n - 1)
    if s[n - 1] > m:
        return s[n - 1]
    return m

if __name__ == "__main__":
    lista = [3, 8, 2, 15, 4, 10]
    print("El máximo es:", maximo(lista, len(lista)))
