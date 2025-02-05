def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
primos = [i for i in range(2, numero + 1) if es_primo(i)]

print("Números primos hasta", numero, ":", primos)