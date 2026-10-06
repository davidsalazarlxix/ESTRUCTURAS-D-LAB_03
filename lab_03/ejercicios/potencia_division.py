# Potencia por division del exponente
def potencia(b, n):
    if n == 0:
        return 1
    mitad = potencia(b, n // 2)
    if n % 2 == 0:
        return mitad * mitad
    return mitad * mitad * b

if __name__ == "__main__":
    base, exp = 2, 10
    print(f"{base}^{exp} =", potencia(base, exp))
