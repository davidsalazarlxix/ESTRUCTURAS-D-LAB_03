# Factorial (Recursivo vs Iterativo)
def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)

def fact_it(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    n = 5
    print(f"Factorial({n}) Rec:", fact_rec(n))
    print(f"Factorial({n}) It:", fact_it(n))
