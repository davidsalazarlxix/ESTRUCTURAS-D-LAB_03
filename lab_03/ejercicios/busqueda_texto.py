# Busqueda de texto
def coincide(p, t, i, j=0):
    if j == len(p):
        return True
    return t[i + j] == p[j] and coincide(p, t, i, j + 1)

def busca_texto(p, t, i=0):
    if i > len(t) - len(p):
        return 0
    if coincide(p, t, i):
        return i + 1
    return busca_texto(p, t, i + 1)

if __name__ == "__main__":
    texto = "algoritmo"
    patron = "rit"
    pos = busca_texto(patron, texto)
    print(f"Patrón '{patron}' encontrado en posición:", pos)
