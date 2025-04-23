def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def n_primos(n):
    count = 0
    for i in range(2, n + 1):
        if eh_primo(i):
            count += 1
    return count

# Testando a função n_primos
print(n_primos(2))    # Deve imprimir 1
print(n_primos(4))    # Deve imprimir 2
print(n_primos(121))  # Deve imprimir 30
