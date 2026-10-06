# Suma mediante incrementos
def suma_inc(a, b):
    if b == 0:
        return a
    return suma_inc(a, b - 1) + 1

if __name__ == "__main__":
    x, y = 7, 5
    print(f"Suma de {x} + {y} =", suma_inc(x, y))
