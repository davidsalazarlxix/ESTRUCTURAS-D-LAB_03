# Actividad 1.4: Multiplicación por el método ruso
def mult_rusa(A, B):
    if A == 0:
        return 0
    if A == 1:
        return B
    if A % 2 != 0:
        return B + mult_rusa(A // 2, B * 2)
    return mult_rusa(A // 2, B * 2)

if __name__ == "__main__":
    print(mult_rusa(18, 7))
    print(mult_rusa(13, 5))