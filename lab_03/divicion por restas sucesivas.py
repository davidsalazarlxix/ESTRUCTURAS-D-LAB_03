# Actividad 1.1: División por restas sucesivas
def division(a, b):
    if b > a:
        return 0
    return division(a - b, b) + 1

if __name__ == "__main__":
    print(division(17, 5))
    print(division(20, 4))