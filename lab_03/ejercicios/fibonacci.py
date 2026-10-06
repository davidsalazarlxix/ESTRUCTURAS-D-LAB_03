# Fibonacci (Recursivo vs Iterativo)
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

def fib_it(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) Rec:", fib_rec(n))
    print(f"Fibonacci({n}) It:", fib_it(n))
