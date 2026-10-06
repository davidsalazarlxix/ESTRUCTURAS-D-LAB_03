# Actividad 1.2: Suma de los dígitos de un número
def sumar_dig(n):
    if n == 0:
        return 0
    return sumar_dig(n // 10) + n % 10

if __name__ == "__main__":
    print(sumar_dig(2026))
    print(sumar_dig(98765))