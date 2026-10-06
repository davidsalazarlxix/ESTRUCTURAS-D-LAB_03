# Caminos del robot (Pasos de 1, 2 y 3 metros)
def caminos_1_2_3(n, pasos=(1, 2, 3)):
    if n == 0:
        return [[]]
    res = []
    for p in pasos:
        if p <= n:
            for c in caminos_1_2_3(n - p, pasos):
                res.append([p] + c)
    return res

if __name__ == "__main__":
    m = 4
    caminos = caminos_1_2_3(m)
    print(f"Caminos para {m}m (pasos 1, 2 y 3):", caminos)
