def eh_hipotenusa(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * i + j * j == n * n:
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for i in range(1, n + 1):
        if eh_hipotenusa(i):
            soma += i
    return soma

# Testando a função soma_hipotenusas
print(soma_hipotenusas(25))  # Deve imprimir 105
