def maior_primo(n):
    def eh_primo(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    maior_primo_encontrado = 0
    for i in range(n, 1, -1):
        if eh_primo(i):
            maior_primo_encontrado = i
            break

    return maior_primo_encontrado

# Exemplos de execução
print(maior_primo(100))  # Saída: 97
print(maior_primo(7))    # Saída: 7
