# Actividad 1.10: Suma de los elementos de una matriz
def suma(fila, col, orden, mat):
    if fila == 0 and col == 0:
        return mat[0][0]
    if col < 0:
        return suma(fila - 1, orden - 1, orden, mat)
    return mat[fila][col] + suma(fila, col - 1, orden, mat)

if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(suma(2, 2, 3, m))