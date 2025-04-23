numero = int(input("Digite um número inteiro: "))

# Verifica se o número é menor ou igual a 1
if numero <= 1:
    print("não primo")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("primo")
    else:
        print("não primo")
