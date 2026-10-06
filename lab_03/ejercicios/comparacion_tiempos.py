# Comparacion de tiempos entre insercion y seleccion
import random
import sys
import time

def insertar(s, j, val):
    if j >= 0 and val < s[j]:
        s[j + 1] = s[j]
        insertar(s, j - 1, val)
    else:
        s[j + 1] = val

def insercion_por_orden(s, n):
    if n <= 1:
        return
    insercion_por_orden(s, n - 1)
    insertar(s, n - 2, s[n - 1])

def seleccion_por_orden(s, i=0):
    if i >= len(s) - 1:
        return
    m = min(range(i, len(s)), key=lambda k: s[k])
    s[i], s[m] = s[m], s[i]
    seleccion_por_orden(s, i + 1)

def comparar_tiempos():
    sys.setrecursionlimit(10000)

    def medir(f, datos):
        d = datos[:]
        t = time.perf_counter()
        f(d)
        return time.perf_counter() - t

    for n in (100, 300):
        casos = {
            "creciente": list(range(n)),
            "decreciente": list(range(n, 0, -1)),
            "aleatorio": random.sample(range(n), n),
        }
        print(f"--- Tamaño N={n} ---")
        for nombre, datos in casos.items():
            t_ins = medir(lambda d: insercion_por_orden(d, len(d)), datos)
            t_sel = medir(seleccion_por_orden, datos)
            print(f"Caso {nombre}: Inserción={t_ins:.5f}s | Selección={t_sel:.5f}s")

if __name__ == "__main__":
    comparar_tiempos()
